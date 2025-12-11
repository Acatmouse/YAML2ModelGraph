"""
yolo_graph.py - Core logic for parsing YAML and generating SVG
"""

import yaml
import math


class SVGBuilder:
    def __init__(self, config):
        self.config = config
        self.elements = []
        self.width = 0
        self.height = 0

    def get_header(self):
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}">
        <style>
            text {{ font-family: "{self.config['font']}"; }}
        </style>
        <defs>
            <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L6,3 z" fill="{self.config["colors"]["line"]}" />
            </marker>
        </defs>
        """

    def add_rect(self, x, y, w, h, fill, label, sub, is_concat=False):
        stroke_w = "1.5" if is_concat else "1.0"
        self.elements.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{self.config["radius"]}" fill="{fill}" stroke="{self.config["colors"]["stroke"]}" stroke-width="{stroke_w}"/>'
        )

        cx, cy = x + w / 2, y + h / 2
        self.elements.append(
            f'<text x="{cx}" y="{cy-7}" font-weight="bold" font-size="14" fill="{self.config["colors"]["text_main"]}" text-anchor="middle" dominant-baseline="middle">{label}</text>'
        )
        self.elements.append(
            f'<text x="{cx}" y="{cy+10}" font-size="11" fill="{self.config["colors"]["text_sub"]}" text-anchor="middle" dominant-baseline="middle">{sub}</text>'
        )
        return {
            "L": (x, cy),
            "R": (x + w, cy),
            "T": (cx, y),
            "B": (cx, y + h),
            "rect": (x, y, w, h),
        }

    def add_bg_lane(self, x, w, h, label, color):
        self.elements.insert(
            0, f'<rect x="{x}" y="30" width="{w}" height="{h-30}" fill="{color}" />'
        )
        # 可选：泳道分割线
        # self.elements.insert(1, f'<line x1="{x}" y1="30" x2="{x}" y2="{h}" stroke="#E0E0E0" stroke-width="1"/>')
        self.elements.append(
            f'<text x="{x+w/2}" y="55" font-weight="bold" font-size="18" fill="{self.config["colors"]["text_main"]}" text-anchor="middle" letter-spacing="1">{label}</text>'
        )

    def add_link(self, p1, p2, dashed=False, routing_type="standard"):
        x1, y1 = p1
        x2, y2 = p2
        dist_x = abs(x2 - x1)
        path = ""

        if routing_type == "vertical_straight":
            path = f"M {x1} {y1} L {x2} {y2}"
        elif routing_type == "manhattan":
            mid_x = (x1 + x2) / 2
            path = f"M {x1} {y1} C {mid_x} {y1}, {mid_x} {y2}, {x2} {y2}"
        elif routing_type == "detour_right":
            offset = 60
            cp1_x = x1 + offset
            cp1_y = y1
            cp2_x = x2 + offset
            cp2_y = y2
            path = f"M {x1} {y1} C {cp1_x} {cp1_y}, {cp2_x} {cp2_y}, {x2} {y2}"
        else:
            cp1_x = x1 + dist_x * 0.5
            cp1_y = y1
            cp2_x = x2 - dist_x * 0.5
            cp2_y = y2
            path = f"M {x1} {y1} C {cp1_x} {cp1_y}, {cp2_x} {cp2_y}, {x2} {y2}"

        dash_attr = 'stroke-dasharray="4,2"' if dashed else ""
        self.elements.append(
            f'<path d="{path}" stroke="{self.config["colors"]["line"]}" stroke-width="1.2" fill="none" {dash_attr} marker-end="url(#arrow)" />'
        )

    def generate(self):
        return self.get_header() + "\n".join(self.elements) + "</svg>"


def parse_and_layout(yaml_path, out_file, config):
    with open(yaml_path, "r") as f:
        d = yaml.safe_load(f)
    full_seq = d.get("backbone", []) + d.get("head", [])
    backbone_len = len(d.get("backbone", []))

    # 1. 解析
    layers = []
    ch = [3]
    curr_stride = 1

    for i, item in enumerate(full_seq):
        f_idx, n, m, args = item
        args = args or []
        m_str = str(m)
        from_idxs = [f_idx] if isinstance(f_idx, int) else list(f_idx)
        abs_from = [(src if src >= 0 else i + src) for src in from_idxs]

        c2 = args[0] if (args and isinstance(args[0], int)) else ch[-1]
        next_stride = curr_stride
        if "Conv" in m_str:
            for a in args:
                if a == 2:
                    next_stride *= 2
                    break
        elif "Upsample" in m_str:
            next_stride /= 2

        col = 0
        if i >= backbone_len:
            if "Detect" in m_str:
                col = 2
            else:
                col = 1

        label = (
            m_str.replace("nn.modules.", "")
            .replace("ularytics.", "")
            .replace("C2f", "C2f")
        )
        if "Conv" in label:
            label = "Conv"

        # 颜色处理：默认使用 fill_node，如果是特殊模块尝试查找特定颜色
        fill = config["colors"]["fill_node"]
        is_concat = False

        # 糖果色主题可能有特殊 key，科研主题统一
        if "Concat" in label:
            fill = config["colors"]["fill_concat"]
            is_concat = True
        elif "Upsample" in label and "fill_upsample" in config["colors"]:
            fill = config["colors"]["fill_upsample"]
        elif "Detect" in label and "fill_detect" in config["colors"]:
            fill = config["colors"]["fill_detect"]

        layers.append(
            {
                "idx": i,
                "label": label,
                "sub": f"{int(next_stride)}x / {c2}c",
                "stride": int(next_stride),
                "col": col,
                "from": abs_from,
                "fill": fill,
                "is_concat": is_concat,
            }
        )
        ch.append(c2)
        curr_stride = next_stride

    # 2. 布局计算
    svg = SVGBuilder(config)
    coords = {}

    # 2.1 Backbone (尺子)
    current_y = 100
    backbone_items = [l for l in layers if l["col"] == 0]

    for l in backbone_items:
        center_x = config["lane_width_bb"] / 2
        props = svg.add_rect(
            center_x - config["node_w"] / 2,
            current_y,
            config["node_w"],
            config["node_h"],
            l["fill"],
            l["label"],
            l["sub"],
            l["is_concat"],
        )
        props["col"] = 0
        props["neck_col_id"] = -1
        coords[l["idx"]] = props
        current_y += config["bb_step"]

    max_bb_y = current_y - config["bb_step"] + config["node_h"]

    # 2.2 Neck (智能多列折叠)
    neck_items = [l for l in layers if l["col"] == 1]
    neck_start_y = 100
    neck_limit_y = max_bb_y
    neck_curr_y = neck_start_y
    neck_col_idx = 0

    neck_cols_layout = [[], [], []]

    for l in neck_items:
        if neck_curr_y > neck_limit_y and neck_col_idx < 2:
            neck_col_idx += 1
            neck_curr_y = neck_start_y
        neck_cols_layout[neck_col_idx].append(l)
        neck_curr_y += config["neck_step"]

    actual_neck_width = 0
    for c_id, items in enumerate(neck_cols_layout):
        if not items:
            continue
        base_x = config["lane_width_bb"] + c_id * (
            config["lane_width_neck_col"] + config["col_gap"]
        )
        center_x = base_x + config["lane_width_neck_col"] / 2
        curr_y = neck_start_y

        for l in items:
            props = svg.add_rect(
                center_x - config["node_w"] / 2,
                curr_y,
                config["node_w"],
                config["node_h"],
                l["fill"],
                l["label"],
                l["sub"],
                l["is_concat"],
            )
            props["col"] = 1
            props["neck_col_id"] = c_id
            coords[l["idx"]] = props
            curr_y += config["neck_step"]

        actual_neck_width = base_x + config["lane_width_neck_col"]

    # 2.3 Head (无缝衔接)
    head_items = [l for l in layers if l["col"] == 2]
    head_start_x = actual_neck_width
    head_curr_y = neck_start_y

    for l in head_items:
        center_x = head_start_x + config["lane_width_head"] / 2

        src_ys = [coords[s]["rect"][1] for s in l["from"] if s in coords]
        target_y = sum(src_ys) / len(src_ys) if src_ys else head_curr_y
        if target_y < head_curr_y:
            target_y = head_curr_y

        props = svg.add_rect(
            center_x - config["node_w"] / 2,
            target_y,
            config["node_w"],
            config["node_h"],
            l["fill"],
            l["label"],
            l["sub"],
            l["is_concat"],
        )
        props["col"] = 2
        props["neck_col_id"] = 99
        coords[l["idx"]] = props
        head_curr_y = target_y + config["neck_step"]

    # 3. 连线
    for l in layers:
        if l["idx"] not in coords:
            continue
        dst = coords[l["idx"]]
        for src_idx in l["from"]:
            if src_idx not in coords:
                continue
            src = coords[src_idx]

            p1 = src["rect"]
            p2 = dst["rect"]
            start_pt = (p1[0] + p1[2], p1[1] + p1[3] / 2)  # Right
            end_pt = (p2[0], p2[1] + p2[3] / 2)  # Left

            dashed = (l["col"] != src["col"]) or abs(l["idx"] - src_idx) > 1
            routing = "standard"

            # Backbone 直连
            if l["col"] == 0 and src["col"] == 0:
                if abs(l["idx"] - src_idx) == 1:
                    start_pt = (p1[0] + p1[2] / 2, p1[1] + p1[3])
                    end_pt = (p2[0] + p2[2] / 2, p2[1])
                    routing = "vertical_straight"
                    dashed = False

            # Backbone -> Neck
            elif src["col"] == 0 and dst["col"] == 1:
                routing = "manhattan"

            # Neck 内部同列
            elif (
                src["col"] == 1
                and dst["col"] == 1
                and src["neck_col_id"] == dst["neck_col_id"]
            ):
                if abs(l["idx"] - src_idx) == 1:
                    start_pt = (p1[0] + p1[2] / 2, p1[1] + p1[3])
                    end_pt = (p2[0] + p2[2] / 2, p2[1])
                    routing = "vertical_straight"
                else:
                    start_pt = (p1[0] + p1[2], p1[1] + p1[3] / 2)
                    end_pt = (p2[0] + p2[2], p2[1] + p2[3] / 2)
                    routing = "detour_right"

            # Head 回连
            elif dst["rect"][0] < src["rect"][0]:
                start_pt = (p1[0], p1[1] + p1[3] / 2)  # Left
                end_pt = (p2[0] + p2[2], p2[1] + p2[3] / 2)  # Right
                routing = "standard"

            svg.add_link(start_pt, end_pt, dashed, routing)

    # 4. 输出
    total_w = head_start_x + config["lane_width_head"]
    svg.width = total_w
    svg.height = max_bb_y + 50

    svg.add_bg_lane(
        0,
        config["lane_width_bb"],
        svg.height,
        "Backbone",
        config["colors"]["bg_backbone"],
    )
    svg.add_bg_lane(
        config["lane_width_bb"],
        head_start_x - config["lane_width_bb"],
        svg.height,
        "Neck",
        config["colors"]["bg_neck"],
    )
    svg.add_bg_lane(
        head_start_x,
        config["lane_width_head"],
        svg.height,
        "Head",
        config["colors"]["bg_head"],
    )

    with open(out_file, "w") as f:
        f.write(svg.generate())
