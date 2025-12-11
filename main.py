#!/usr/bin/env python3
"""
YOLO Graph Generator
Usage:
    python main.py model.yaml [output.svg] [--theme paper|candy|dark]
"""

import sys
import themes
import yolo_graph


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python main.py model.yaml [output.svg] [--theme paper|candy|dark]"
        )
        return

    yaml_path = sys.argv[1]

    # 默认输出文件名
    out_name = "yolo_graph.svg"
    if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
        out_name = sys.argv[2]
        if not out_name.endswith(".svg"):
            out_name += ".svg"

    # 解析主题参数
    theme_name = "paper"  # 默认主题
    if "--theme" in sys.argv:
        try:
            idx = sys.argv.index("--theme")
            theme_name = sys.argv[idx + 1]
        except IndexError:
            print("Error: --theme requires an argument (paper, candy, dark)")
            return

    # 获取配置
    config = themes.get_config(theme_name)

    print(f"🎨 Generating graph using theme: '{theme_name}'")
    try:
        yolo_graph.parse_and_layout(yaml_path, out_name, config)
        print(f"✅ Successfully saved to {out_name}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
