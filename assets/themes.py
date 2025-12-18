"""Predefined color themes for charts with typography."""

from typing import Dict, Any


THEMES = {
    'Light': {
        'background': '#FFFFFF',
        'grid': '#CCCCCC',
        'text': '#000000',
        'axis': '#000000',
        'font_family': 'sans-serif',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#1f77b4',  # Blue
            '#ff7f0e',  # Orange
            '#2ca02c',  # Green
            '#d62728',  # Red
            '#9467bd',  # Purple
            '#8c564b',  # Brown
            '#e377c2',  # Pink
            '#7f7f7f',  # Gray
            '#bcbd22',  # Olive
            '#17becf',  # Cyan
        ]
    },
    'Dark': {
        'background': '#1E1E1E',
        'grid': '#404040',
        'text': '#FFFFFF',
        'axis': '#FFFFFF',
        'font_family': 'sans-serif',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#4A9EFF',  # Bright Blue
            '#FFA94D',  # Bright Orange
            '#51CF66',  # Bright Green
            '#FF6B6B',  # Bright Red
            '#BA8FFF',  # Bright Purple
            '#FFD43B',  # Bright Yellow
            '#FF8787',  # Bright Pink
            '#94D82D',  # Bright Lime
            '#66D9EF',  # Bright Cyan
            '#FFB84D',  # Bright Amber
        ]
    },
    'IMF Professional': {
        'background': '#FFFFFF',
        'grid': '#E5E5E5',
        'text': '#1A1A1A',
        'axis': '#333333',
        'font_family': 'Arial',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#004B7B',  # IMF Navy Blue
            '#1565C0',  # IMF Deep Blue
            '#0097A7',  # IMF Cyan
            '#00796B',  # IMF Teal
            '#F57C00',  # IMF Orange
            '#D32F2F',  # IMF Red
            '#7B1FA2',  # IMF Purple
            '#5E35B1',  # IMF Indigo
            '#1976D2',  # IMF Bright Blue
            '#00BCD4',  # IMF Light Cyan
        ]
    },
    'IMF Report': {
        'background': '#FAFAFA',
        'grid': '#D0D0D0',
        'text': '#1A1A1A',
        'axis': '#333333',
        'font_family': 'Times New Roman',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#004B7B',  # IMF Primary Blue
            '#E53935',  # Report Red
            '#388E3C',  # Report Green
            '#F57C00',  # Report Orange
        ]
    },
    'World Bank Official': {
        'background': '#FFFFFF',
        'grid': '#E0E0E0',
        'text': '#212121',
        'axis': '#424242',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#003478',  # World Bank Dark Blue
            '#0C5AA0',  # World Bank Primary Blue
            '#1E88E5',  # World Bank Bright Blue
            '#00897B',  # World Bank Teal
            '#F57F17',  # World Bank Amber
            '#D32F2F',  # World Bank Red
            '#512DA8',  # World Bank Deep Purple
            '#388E3C',  # World Bank Green
            '#1976D2',  # World Bank Sky Blue
            '#C62828',  # World Bank Dark Red
        ]
    },
    'World Bank Elegant': {
        'background': '#F5F5F5',
        'grid': '#BDBDBD',
        'text': '#1A1A1A',
        'axis': '#333333',
        'font_family': 'Garamond',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#003478',  # World Bank Primary
            '#0C5AA0',  # World Bank Secondary
            '#424242',  # Charcoal
            '#00897B',  # Teal
            '#F57F17',  # Amber
        ]
    },

    'Publication': {
        'background': '#FFFFFF',
        'grid': '#DDDDDD',
        'text': '#000000',
        'axis': '#000000',
        'font_family': 'serif',
        'font_size': 9,
        'title_fontsize': 14,
        'title_fontweight': 'bold',
        'line_colors': [
            '#000000',  # Black
            '#CC0000',  # Red
            '#0000CC',  # Blue
            '#00CC00',  # Green
            '#FF9900',  # Orange
            '#9900CC',  # Purple
            '#00CCCC',  # Cyan
            '#CC00CC',  # Magenta
            '#666666',  # Dark Gray
            '#333333',  # Very Dark Gray
        ]
    },
    'Accessible (Colorblind Safe)': {
        'background': '#FFFFFF',
        'grid': '#D0D0D0',
        'text': '#000000',
        'axis': '#000000',
        'font_family': 'Segoe UI',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#0072B2',  # Blue
            '#D55E00',  # Vermillion
            '#E69F00',  # Orange
            '#009E73',  # Green
            '#F0E442',  # Yellow
            '#56B4E9',  # Sky Blue
            '#CC79A7',  # Reddish Purple
            '#000000',  # Black
        ]
    },
}


def get_theme(theme_name: str) -> Dict[str, Any]:
    """
    Get a theme by name.
    
    Args:
        theme_name: Name of the theme
        
    Returns:
        Theme dictionary
        
    Raises:
        ValueError: If theme doesn't exist
    """
    if theme_name not in THEMES:
        available = ', '.join(THEMES.keys())
        raise ValueError(f"Theme '{theme_name}' not found. Available themes: {available}")
    
    return THEMES[theme_name].copy()


def get_theme_names() -> list:
    """
    Get list of available theme names.
    
    Returns:
        List of theme names
    """
    return list(THEMES.keys())


SPECIAL_PRESETS = {
    'COVID-19': {
        'description': 'Highlight COVID-19 period (2020-2021)',
        'period_highlights': [
            {
                'name': 'COVID-19',
                'start': 2020,
                'end': 2021,
                'color': '#FF6B6B',
                'alpha': 0.15,
                'label': 'COVID-19 Period'
            }
        ]
    },
    'Great Recession': {
        'description': 'Highlight Great Recession (2008-2009)',
        'period_highlights': [
            {
                'name': 'Great Recession',
                'start': 2008,
                'end': 2009,
                'color': '#8B4513',
                'alpha': 0.12,
                'label': 'Great Recession'
            }
        ]
    },
    'Housing Crisis': {
        'description': 'Highlight Housing Market Crisis (2007-2012)',
        'period_highlights': [
            {
                'name': 'Housing Crisis',
                'start': 2007,
                'end': 2012,
                'color': '#DC143C',
                'alpha': 0.1,
                'label': 'Housing Crisis'
            }
        ]
    },
    'Interest Rate Hikes': {
        'description': 'Highlight recent rate increase period',
        'period_highlights': [
            {
                'name': 'Rate Hikes',
                'start': 2022,
                'end': 2023,
                'color': '#FFD700',
                'alpha': 0.15,
                'label': 'Rate Increase Period'
            }
        ]
    }
}


def get_special_preset(preset_name: str) -> Dict[str, Any]:
    """Get a special scenario preset."""
    if preset_name not in SPECIAL_PRESETS:
        available = ', '.join(SPECIAL_PRESETS.keys())
        raise ValueError(f"Preset '{preset_name}' not found. Available: {available}")
    return SPECIAL_PRESETS[preset_name].copy()


def get_preset_names() -> list:
    """Get list of available special presets."""
    return list(SPECIAL_PRESETS.keys())
