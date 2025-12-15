"""
themes.py - Color schemes and layout configurations for YOLO Graph
"""

# ================= 基础布局参数 (DO NOT CHANGE) =================
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
    # Default gradients (flat white for compatibility)
    "gradients": {
        "grad_bb_start": "#FFFFFF", "grad_bb_end": "#FFFFFF",
        "grad_neck_start": "#FFFFFF", "grad_neck_end": "#FFFFFF",
        "grad_head_start": "#FFFFFF", "grad_head_end": "#FFFFFF",
        "grad_concat_start": "#FFFFFF", "grad_concat_end": "#FFFFFF",
        "grad_node_start": "#FFFFFF", "grad_node_end": "#FFFFFF",
    }
}

# ================= 主题定义 =================

# 1. 科研黑白灰 (Paper / Academic) - 默认
THEME_PAPER = {
    "colors": {
        "bg_backbone": "#FAFAFA", "bg_neck": "#FFFFFF", "bg_head": "#FAFAFA",
        "stroke": "#000000", "line": "#333333",
        "fill_node": "#FFFFFF", "fill_concat": "#F0F0F0",
        "text_main": "#000000", "text_sub": "#444444",
    },
    "gradients": {
        "grad_bb_start": "#FFFFFF", "grad_bb_end": "#F5F5F5",
        "grad_neck_start": "#FFFFFF", "grad_neck_end": "#FFFFFF",
        "grad_head_start": "#FFFFFF", "grad_head_end": "#F5F5F5",
        "grad_concat_start": "#F0F0F0", "grad_concat_end": "#E0E0E0",
        "grad_node_start": "#FFFFFF", "grad_node_end": "#F9F9F9",
    },
    # Standard academic colors for strips
    "type_colors": {
        "Conv":     "#2196F3", # Blue
        "Concat":   "#FFC107", # Yellow
        "Detect":   "#F44336", # Red
        "Upsample": "#4CAF50", # Green
        "C2f":      "#9E9E9E", # Grey
        "Other":    "#607D8B"  # Dark Grey
    },
    "font": "Times New Roman, serif",
}

# 2. 糖果色 (Candy / Pastel)
THEME_CANDY = {
    "colors": {
        "bg_backbone": "#F0F4F8", "bg_neck": "#FFF8F0", "bg_head": "#F3F0F5",
        "stroke": "#546E7A", "line": "#607D8B",
        "fill_node": "#FFFFFF", "fill_concat": "#FFF9C4",
        "fill_upsample": "#E1F5FE", "fill_detect": "#FFEBEE",
        "text_main": "#263238", "text_sub": "#78909C",
    },
    "gradients": {
        "grad_bb_start": "#FFFFFF", "grad_bb_end": "#FFFFFF",
        "grad_neck_start": "#FFFFFF", "grad_neck_end": "#FFFFFF",
        "grad_head_start": "#FFFFFF", "grad_head_end": "#FFFFFF",
        "grad_concat_start": "#FFF9C4", "grad_concat_end": "#FFF59D",
        "grad_node_start": "#FFFFFF", "grad_node_end": "#FFFFFF",
    },
    # Soft Pastel Strips
    "type_colors": {
        "Conv":     "#64B5F6", # Soft Blue
        "Concat":   "#FFD54F", # Soft Yellow
        "Detect":   "#E57373", # Soft Red
        "Upsample": "#81C784", # Soft Green
        "C2f":      "#B0BEC5", # Soft Grey
        "Other":    "#90A4AE"
    },
    "font": "Arial, sans-serif",
    "radius": 6,
}

# 3. 暗黑极客 (Dark / Neon)
THEME_DARK = {
    "colors": {
        "bg_backbone": "#1E1E1E", "bg_neck": "#252526", "bg_head": "#1E1E1E",
        "stroke": "#61AFEF", "line": "#ABB2BF",
        "fill_node": "#2D3135", "fill_concat": "#3E4451",
        "text_main": "#E5C07B", "text_sub": "#98C379",
    },
    "gradients": {
        "grad_bb_start": "#2D3135", "grad_bb_end": "#21252B",
        "grad_neck_start": "#2D3135", "grad_neck_end": "#21252B",
        "grad_head_start": "#2D3135", "grad_head_end": "#21252B",
        "grad_concat_start": "#3E4451", "grad_concat_end": "#323844",
        "grad_node_start": "#2D3135", "grad_node_end": "#21252B",
    },
    # Neon Strips
    "type_colors": {
        "Conv":     "#61AFEF", # Neon Blue
        "Concat":   "#E5C07B", # Neon Yellow
        "Detect":   "#E06C75", # Neon Red
        "Upsample": "#98C379", # Neon Green
        "C2f":      "#5C6370", # Grey
        "Other":    "#56B6C2"  # Cyan
    },
    "font": "Consolas, monospace",
    "radius": 4,
}

# 4. 极简海洋 (Ocean / Tech)
THEME_OCEAN = {
    "colors": {
        "bg_backbone": "#E1F5FE", "bg_neck": "#F0F4C3", "bg_head": "#E1F5FE",
        "stroke": "#0277BD", "line": "#0288D1",
        "fill_node": "#FFFFFF", "fill_concat": "#B3E5FC",
        "fill_upsample": "#E0F7FA", "fill_detect": "#FFCCBC",
        "text_main": "#01579B", "text_sub": "#455A64",
    },
    "type_colors": {
        "Conv":     "#0288D1", 
        "Concat":   "#FBC02D", 
        "Detect":   "#FF7043", 
        "Upsample": "#0097A7", 
        "C2f":      "#78909C", 
        "Other":    "#546E7A"
    },
    "font": "Verdana, Geneva, sans-serif",
    "radius": 5,
}

# 5. 复古暖阳 (Retro / Gruvbox)
THEME_RETRO = {
    "colors": {
        "bg_backbone": "#FBF1C7", "bg_neck": "#EBDBB2", "bg_head": "#FBF1C7",
        "stroke": "#3C3836", "line": "#504945",
        "fill_node": "#F9F5D7", "fill_concat": "#FABD2F",
        "fill_detect": "#FB4934",
        "text_main": "#282828", "text_sub": "#928374",
    },
    "type_colors": {
        "Conv":     "#458588", # Teal
        "Concat":   "#D79921", # Yellow
        "Detect":   "#CC241D", # Red
        "Upsample": "#98971A", # Green
        "C2f":      "#A89984", # Grey
        "Other":    "#689D6A"  # Aqua
    },
    "font": "Consolas, 'Courier New', monospace",
    "radius": 3,
}

# 6. 工程蓝图 (Blueprint)
THEME_BLUEPRINT = {
    "colors": {
        "bg_backbone": "#2B3A42", "bg_neck": "#3F5765", "bg_head": "#2B3A42",
        "stroke": "#FFFFFF", "line": "#E0E0E0",
        "fill_node": "#2B3A42", "fill_concat": "#3F5765",
        "text_main": "#FFFFFF", "text_sub": "#BDC3C7",
    },
    "type_colors": {
        "Conv":     "#29B6F6", 
        "Concat":   "#FFEE58", 
        "Detect":   "#EF5350", 
        "Upsample": "#66BB6A", 
        "C2f":      "#BDBDBD", 
        "Other":    "#78909C"
    },
    "font": "Osifont, 'ISOCPEUR', 'Courier New', sans-serif",
    "radius": 0,
}

# 7. 森林氧吧 (Forest / Nature)
THEME_FOREST = {
    "colors": {
        "bg_backbone": "#E8F5E9", "bg_neck": "#F1F8E9", "bg_head": "#E8F5E9",
        "stroke": "#2E7D32", "line": "#388E3C",
        "fill_node": "#FFFFFF", "fill_concat": "#C8E6C9",
        "text_main": "#1B5E20", "text_sub": "#558B2F",
    },
    "type_colors": {
        "Conv":     "#66BB6A", 
        "Concat":   "#FFEB3B", 
        "Detect":   "#FF7043", 
        "Upsample": "#43A047", 
        "C2f":      "#8D6E63", 
        "Other":    "#7CB342"
    },
    "font": "Georgia, serif",
    "radius": 8,
}

# 8. 学术三原色 (Academic RYB)
THEME_PAPER_RYB = {
    "colors": {
        "bg_backbone": "#EBF5FB", "bg_neck": "#FEF9E7", "bg_head": "#FADBD8",
        "stroke": "#2C3E50", "line": "#34495E",
        "fill_node": "#FFFFFF", "fill_concat": "#FFF3E0",
        "text_main": "#17202A", "text_sub": "#566573",
    },
    "type_colors": {
        "Conv":     "#2980B9", 
        "Concat":   "#F39C12", 
        "Detect":   "#C0392B", 
        "Upsample": "#27AE60", 
        "C2f":      "#7F8C8D", 
        "Other":    "#34495E"
    },
    "font": "Times New Roman, serif",
    "radius": 2,
}

# 9. 现代期刊 (Modern Journal)
THEME_JOURNAL = {
    "colors": {
        "bg_backbone": "#F5F7FA", "bg_neck": "#FFFFFF", "bg_head": "#F5F7FA",
        "stroke": "#333333", "line": "#222222",
        "fill_node": "#FFFFFF", "fill_concat": "#E0F2F1", "fill_detect": "#F3E5F5",
        "text_main": "#000000", "text_sub": "#424242",
    },
    "type_colors": {
        "Conv":     "#00ACC1", 
        "Concat":   "#FFB300", 
        "Detect":   "#D81B60", 
        "Upsample": "#43A047", 
        "C2f":      "#757575", 
        "Other":    "#546E7A"
    },
    "font": "Times New Roman, serif",
    "radius": 0,
}

# 主题注册表
THEMES = {
    "paper": THEME_PAPER,
    "candy": THEME_CANDY,
    "dark": THEME_DARK,
    "ocean": THEME_OCEAN,
    "retro": THEME_RETRO,
    "blueprint": THEME_BLUEPRINT,
    "forest": THEME_FOREST,
    "paper_ryb": THEME_PAPER_RYB,
    "journal": THEME_JOURNAL
}

def get_config(theme_name="paper"):
    """合并默认布局和选定主题"""
    base = DEFAULT_LAYOUT.copy()
    # Default to paper if theme not found
    theme = THEMES.get(theme_name, THEME_PAPER)

    # 允许主题覆盖默认布局参数
    for k, v in theme.items():
        if k in base:
            base[k] = v

    config = base.copy()
    config["colors"] = theme["colors"]
    config["font"] = theme["font"]
    
    # Merge gradients
    theme_grads = theme.get("gradients", {})
    default_grads = base["gradients"]
    config["gradients"] = {**default_grads, **theme_grads}

    if "radius" in theme:
        config["radius"] = theme["radius"]
        
    # Inject type_colors, fallback to Paper defaults if missing in theme
    config["type_colors"] = theme.get("type_colors", THEME_PAPER["type_colors"])

    return config