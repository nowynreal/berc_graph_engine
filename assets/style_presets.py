"""Professional style presets for charts."""

from typing import Dict, Any


STYLE_PRESETS = {
    'Professional Clean': {
        'description': 'Professional style with horizontal grid lines (X-axis)',
        'background_color': '#FFFFFF',
        'grid_color': '#D0D0D0',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'grid_type': 'x_only',
        'show_grid': True,
        'legend_position': 'upper right',
    },
    'Analytical Grid': {
        'description': 'Analytical style with vertical grid lines (Y-axis)',
        'background_color': '#FFFFFF',
        'grid_color': '#D5D5D5',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'grid_type': 'y_only',
        'show_grid': True,
        'legend_position': 'best',
    },
    'IMF Official': {
        'description': 'IMF-style professional presentation',
        'background_color': '#FFFFFF',
        'grid_color': '#D5D5D5',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'grid_type': 'x_only',
        'show_grid': True,
        'legend_position': 'best',
    },
    'World Bank Report': {
        'description': 'World Bank publication style',
        'background_color': '#FAFAFA',
        'grid_color': '#D0D0D0',
        'font_family': 'Garamond',
        'font_size': 10,
        'title_fontsize': 18,
        'grid_type': 'x_only',
        'show_grid': True,
        'legend_position': 'lower right',
    },
    'Minimal Grid': {
        'description': 'Minimal design with very light grid',
        'background_color': '#FFFFFF',
        'grid_color': '#E8E8E8',
        'font_family': 'Helvetica',
        'font_size': 10,
        'title_fontsize': 16,
        'grid_type': 'x_only',
        'show_grid': True,
        'legend_position': 'best',
    },
    'Full Grid': {
        'description': 'Both X and Y axis gridlines',
        'background_color': '#FFFFFF',
        'grid_color': '#CCCCCC',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 16,
        'grid_type': 'both',
        'show_grid': True,
        'legend_position': 'best',
    },
    'Academic Journal': {
        'description': 'Style for academic publications',
        'background_color': '#FFFFFF',
        'grid_color': '#E0E0E0',
        'font_family': 'Times New Roman',
        'font_size': 10,
        'title_fontsize': 14,
        'grid_type': 'y_only',
        'show_grid': True,
        'legend_position': 'best',
    },
    'Presentation': {
        'description': 'Clean presentation style',
        'background_color': '#FAFAFA',
        'grid_color': '#E0E0E0',
        'font_family': 'Arial',
        'font_size': 12,
        'title_fontsize': 22,
        'grid_type': 'x_only',
        'show_grid': True,
        'legend_position': 'upper right',
    },
    'No Grid': {
        'description': 'Clean style without grid',
        'background_color': '#FFFFFF',
        'grid_color': '#FFFFFF',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 16,
        'grid_type': 'none',
        'show_grid': False,
        'legend_position': 'best',
    },
}


def get_preset(preset_name: str) -> Dict[str, Any]:
    """
    Get a style preset by name.
    
    Args:
        preset_name: Name of the preset
        
    Returns:
        Preset dictionary
        
    Raises:
        ValueError: If preset doesn't exist
    """
    if preset_name not in STYLE_PRESETS:
        available = ', '.join(STYLE_PRESETS.keys())
        raise ValueError(f"Preset '{preset_name}' not found. Available presets: {available}")
    
    return STYLE_PRESETS[preset_name].copy()


def get_preset_names() -> list:
    """
    Get list of available preset names.
    
    Returns:
        List of preset names
    """
    return list(STYLE_PRESETS.keys())
