"""
themes.py - Color schemes and layout configurations for YOLO Graph
"""

# 基础布局参数
DEFAULT_LAYOUT = {
    "lane_width_bb": 220,
    "lane_width_neck_col": 220,
    "lane_width_head": 220,
    "node_w": 150,
    "node_h": 44,
    "radius": 0,
    "bb_step": 80,
    "neck_step": 120,
    "col_gap": 80,
}

# 主题 1: 科研黑白灰 (Paper / Academic) - 默认
THEME_PAPER = {
    "colors": {
        "bg_backbone": "#FAFAFA",
        "bg_neck": "#FFFFFF",
        "bg_head": "#FAFAFA",
        "stroke": "#000000",
        "line": "#333333",
        "fill_node": "#FFFFFF",
        "fill_concat": "#F0F0F0",
        "text_main": "#000000",
        "text_sub": "#444444",
    },
    "font": "Times New Roman, serif",
}

# 主题 2: 糖果色 (Candy / Pastel) - 您之前的偏好
THEME_CANDY = {
    "colors": {
        "bg_backbone": "#F0F4F8",  # 淡蓝灰背景
        "bg_neck": "#FFF8F0",  # 淡橙背景
        "bg_head": "#F3F0F5",  # 淡紫背景
        "stroke": "#546E7A",  # 蓝灰边框
        "line": "#607D8B",  # 蓝灰线条
        "fill_node": "#FFFFFF",
        "fill_concat": "#FFF9C4",  # 柠檬黄
        "fill_upsample": "#E1F5FE",  # 浅蓝
        "fill_detect": "#FFEBEE",  # 浅红
        "text_main": "#263238",
        "text_sub": "#78909C",
    },
    "font": "Arial, sans-serif",  # 糖果色配无衬线字体更现代
    "radius": 6,  # 糖果色配圆角更好看
}

# 主题 3: 暗黑极客 (Dark / Neon) - 适合屏幕演示
THEME_DARK = {
    "colors": {
        "bg_backbone": "#1E1E1E",
        "bg_neck": "#252526",
        "bg_head": "#1E1E1E",
        "stroke": "#61AFEF",  # 蓝色边框
        "line": "#ABB2BF",  # 灰色线条
        "fill_node": "#2D3135",
        "fill_concat": "#3E4451",
        "text_main": "#E5C07B",  # 金色文字
        "text_sub": "#98C379",  # 绿色副标题
    },
    "font": "Consolas, monospace",  # 代码字体
    "radius": 4,
}
# 主题 4: 极简海洋 (Ocean / Tech)
THEME_OCEAN = {
    "colors": {
        "bg_backbone": "#E1F5FE",  # 极浅蓝
        "bg_neck": "#F0F4C3",  # 极浅青柠 (区分Neck)
        "bg_head": "#E1F5FE",
        "stroke": "#0277BD",  # 以此深蓝做边框
        "line": "#0288D1",  # 亮蓝线条
        "fill_node": "#FFFFFF",
        "fill_concat": "#B3E5FC",  # 高亮浅蓝
        "fill_upsample": "#E0F7FA",
        "fill_detect": "#FFCCBC",  # 也是一种强调
        "text_main": "#01579B",  # 深蓝文字
        "text_sub": "#455A64",  # 蓝灰副标题
    },
    "font": "Verdana, Geneva, sans-serif",
    "radius": 5,
}

# 主题 5: 复古暖阳 (Retro / Gruvbox)
THEME_RETRO = {
    "colors": {
        "bg_backbone": "#FBF1C7",  # 暖米色
        "bg_neck": "#EBDBB2",  # 稍深一点的米色
        "bg_head": "#FBF1C7",
        "stroke": "#3C3836",  # 深褐灰
        "line": "#504945",
        "fill_node": "#F9F5D7",
        "fill_concat": "#FABD2F",  # 复古黄
        "fill_detect": "#FB4934",  # 复古红
        "text_main": "#282828",  # 近黑
        "text_sub": "#928374",  # 灰褐
    },
    "font": "Consolas, 'Courier New', monospace",  # 等宽字体更有复古感
    "radius": 3,
}

# 主题 6: 工程蓝图 (Blueprint)
THEME_BLUEPRINT = {
    "colors": {
        "bg_backbone": "#2B3A42",  # 深蓝灰
        "bg_neck": "#3F5765",  # 稍亮的蓝灰
        "bg_head": "#2B3A42",
        "stroke": "#FFFFFF",  # 白色边框
        "line": "#E0E0E0",  # 银白线条
        "fill_node": "#2B3A42",  # 与背景同色(镂空感)
        "fill_concat": "#3F5765",  # 稍微区分
        "text_main": "#FFFFFF",  # 白字
        "text_sub": "#BDC3C7",  # 银灰字
    },
    "font": "Osifont, 'ISOCPEUR', 'Courier New', sans-serif",  # 尝试工程字体
    "radius": 0,  # 绝对直角
}

# 主题 7: 森林氧吧 (Forest / Nature)
THEME_FOREST = {
    "colors": {
        "bg_backbone": "#E8F5E9",  # 浅绿
        "bg_neck": "#F1F8E9",  # 浅嫩草色
        "bg_head": "#E8F5E9",
        "stroke": "#2E7D32",  # 深绿边框
        "line": "#388E3C",
        "fill_node": "#FFFFFF",
        "fill_concat": "#C8E6C9",  # 高亮绿
        "text_main": "#1B5E20",  # 深绿文字
        "text_sub": "#558B2F",
    },
    "font": "Georgia, serif",
    "radius": 8,  # 大圆角
}

# 主题 8: 学术三原色 (Academic RYB)
THEME_PAPER_RYB = {
    "colors": {
        # 极淡的红黄蓝背景，打印友好
        "bg_backbone": "#EBF5FB",  # 淡雅蓝 (Backbone)
        "bg_neck": "#FEF9E7",  # 羊皮纸黄 (Neck)
        "bg_head": "#FADBD8",  # 藕粉红 (Head)
        "stroke": "#2C3E50",  # 普鲁士蓝灰 (比纯黑更有质感)
        "line": "#34495E",  # 深灰蓝线条
        "fill_node": "#FFFFFF",  # 节点保持纯白，突出内容
        "fill_concat": "#FFF3E0",  # 极淡的橙色高亮 Concat
        "text_main": "#17202A",  # 墨黑
        "text_sub": "#566573",  # 铁灰
    },
    "font": "Times New Roman, serif",
    "radius": 2,  # 微圆角，既严谨又不生硬
}

# 主题 9: 现代期刊 (Modern Journal / Springer)
THEME_JOURNAL = {
    "colors": {
        # 极其克制的背景色
        "bg_backbone": "#F5F7FA",  # 冷灰白
        "bg_neck": "#FFFFFF",  # 纯白 (突出中间融合部分)
        "bg_head": "#F5F7FA",  # 冷灰白 (呼应首尾)
        "stroke": "#333333",  # 深炭灰边框
        "line": "#222222",  # 近黑连线
        "fill_node": "#FFFFFF",
        # 在极简风格下，用淡青色和淡紫色来区分特殊模块
        "fill_concat": "#E0F2F1",  # 淡青 (Teal 50)
        "fill_detect": "#F3E5F5",  # 淡紫 (Purple 50)
        "text_main": "#000000",
        "text_sub": "#424242",
    },
    "font": "Times New Roman, serif",  # 必须是衬线体
    "radius": 0,  # 直角，最严谨的风格
}

# 主题注册表
THEMES = {
    "paper": THEME_PAPER,       # 默认论文
    "candy": THEME_CANDY,       # 糖果色
    "dark": THEME_DARK,         # 暗黑
    "ocean": THEME_OCEAN,       # 海洋
    "retro": THEME_RETRO,       # 复古
    "blueprint": THEME_BLUEPRINT, # 蓝图
    "forest": THEME_FOREST,     # 森林
    "paper_ryb": THEME_PAPER_RYB, # 淡红黄蓝 (推荐!)
    "journal": THEME_JOURNAL      # 极简期刊风
}


def get_config(theme_name="paper"):
    """合并默认布局和选定主题"""
    base = DEFAULT_LAYOUT.copy()
    theme = THEMES.get(theme_name, THEME_PAPER)

    # 允许主题覆盖默认布局参数 (例如圆角)
    for k, v in theme.items():
        if k in base:
            base[k] = v

    # 合并颜色和字体
    config = base.copy()
    config["colors"] = theme["colors"]
    config["font"] = theme["font"]

    # 如果主题定义了额外的 radius (如糖果色)，确保它被应用
    if "radius" in theme:
        config["radius"] = theme["radius"]

    return config
