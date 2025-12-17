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
    'Scientific': {
        'background': '#F5F5F5',
        'grid': '#B0B0B0',
        'text': '#2C2C2C',
        'axis': '#2C2C2C',
        'font_family': 'serif',
        'font_size': 9,
        'title_fontsize': 14,
        'title_fontweight': 'bold',
        'line_colors': [
            '#0063B2',  # Deep Blue
            '#9CC3D5',  # Light Blue
            '#DC143C',  # Crimson
            '#00A08A',  # Teal
            '#F2AD00',  # Gold
            '#5BBCD6',  # Sky Blue
            '#F98400',  # Dark Orange
            '#00A896',  # Turquoise
            '#FF6F59',  # Coral
            '#046C9A',  # Ocean Blue
        ]
    },
    'Vibrant': {
        'background': '#FAFAFA',
        'grid': '#E0E0E0',
        'text': '#212121',
        'axis': '#212121',
        'font_family': 'sans-serif',
        'font_size': 10,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#E91E63',  # Pink
            '#9C27B0',  # Purple
            '#3F51B5',  # Indigo
            '#00BCD4',  # Cyan
            '#4CAF50',  # Green
            '#FFEB3B',  # Yellow
            '#FF9800',  # Orange
            '#F44336',  # Red
            '#009688',  # Teal
            '#673AB7',  # Deep Purple
        ]
    },
    'Pastel': {
        'background': '#FFFFFF',
        'grid': '#D0D0D0',
        'text': '#333333',
        'axis': '#333333',
        'font_family': 'sans-serif',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'normal',
        'line_colors': [
            '#AEC6CF',  # Pastel Blue
            '#FFB347',  # Pastel Orange
            '#B39EB5',  # Pastel Purple
            '#FF6961',  # Pastel Red
            '#77DD77',  # Pastel Green
            '#FDFD96',  # Pastel Yellow
            '#FFD1DC',  # Pastel Pink
            '#C1E1C1',  # Pastel Mint
            '#CFCFC4',  # Pastel Gray
            '#FFE5B4',  # Pastel Peach
        ]
    },
    'Monochrome': {
        'background': '#FFFFFF',
        'grid': '#CCCCCC',
        'text': '#000000',
        'axis': '#000000',
        'font_family': 'sans-serif',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#000000',  # Black
            '#4A4A4A',  # Dark Gray
            '#6E6E6E',  # Gray
            '#929292',  # Medium Gray
            '#B6B6B6',  # Light Gray
            '#333333',  # Very Dark Gray
            '#595959',  # Charcoal
            '#808080',  # Gray
            '#A8A8A8',  # Silver
            '#CCCCCC',  # Light Silver
        ]
    },
    'MTSU Blue': {
        'background': '#FFFFFF',
        'grid': '#E8E8E8',
        'text': '#002B5C',  # MTSU Dark Blue
        'axis': '#002B5C',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#002B5C',  # MTSU Dark Blue
            '#0055B8',  # MTSU Bright Blue
            '#DD6108',  # MTSU Orange
            '#6C757D',  # Gray
            '#28A745',  # Green
            '#FFC720',  # Gold
            '#FF6B6B',  # Red
            '#17A2B8',  # Cyan
            '#6F42C1',  # Purple
            '#E83E8C',  # Pink
        ]
    },
    'MTSU Bold': {
        'background': '#FFFFFF',
        'grid': '#D9D9D9',
        'text': '#002B5C',
        'axis': '#002B5C',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'line_colors': [
            '#C00000',  # Bold Red
            '#0055B8',  # MTSU Bright Blue
            '#6C757D',  # Gray
            '#28A745',  # Green
            '#FFC720',  # Gold
        ]
    },
    'MTSU Publication': {
        'background': '#FFFFFF',
        'grid': '#E6E6E6',
        'text': '#1A1A1A',
        'axis': '#1A1A1A',
        'font_family': 'Times New Roman',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#C00000',  # Publication Red
            '#1F4E78',  # Publication Blue
            '#70AD47',  # Publication Green
            '#ED7D31',  # Publication Orange
        ]
    },
    'BERC Professional': {
        'background': '#F8F9FA',
        'grid': '#D4D7DC',
        'text': '#1A1A1A',
        'axis': '#333333',
        'font_family': 'Arial',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#003366',  # Navy Blue
            '#006699',  # Blue
            '#0099CC',  # Light Blue
            '#00CC99',  # Teal
            '#99CC00',  # Lime
            '#FFCC00',  # Gold
            '#FF9900',  # Orange
            '#FF6600',  # Dark Orange
            '#CC3300',  # Red
            '#993366',  # Mauve
        ]
    },
    'BERC Report': {
        'background': '#FFFFFF',
        'grid': '#D4D7DC',
        'text': '#1A1A1A',
        'axis': '#333333',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'line_colors': [
            '#C00000',  # Report Red
            '#1F77B4',  # Report Blue
            '#2CA02C',  # Green
            '#FF7F0E',  # Orange
        ]
    },
    'BERC Dark': {
        'background': '#101216',
        'grid': '#2B2F36',
        'text': '#FFFFFF',
        'axis': '#FFFFFF',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'line_colors': [
            '#FF6B6B',  # Red
            '#4A9EFF',  # Blue
            '#51CF66',  # Green
            '#FFA94D',  # Orange
        ]
    },
    'BERC Nashville': {
        'background': '#FFFFFF',
        'grid': '#DEDEDE',
        'text': '#000000',
        'axis': '#000000',
        'font_family': 'Arial',
        'font_size': 12,
        'title_fontsize': 22,
        'title_fontweight': 'bold',
        'line_colors': [
            '#C00000',  # Closings (Red)
            '#1F77B4',  # Inventory (Blue)
            '#6C757D',  # Gray
            '#28A745',  # Green
        ]
    },
    'BERC Modern': {
        'background': '#FFFFFF',
        'grid': '#E0E0E0',
        'text': '#2C3E50',
        'axis': '#2C3E50',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#1E90FF',  # Dodger Blue
            '#FF6347',  # Tomato
            '#32CD32',  # Lime Green
            '#FFD700',  # Gold
            '#8A2BE2',  # Blue Violet
            '#00CED1',  # Dark Turquoise
            '#FF4500',  # Orange Red
            '#2E8B57',  # Sea Green
            '#DC143C',  # Crimson
            '#4169E1',  # Royal Blue
        ]
    },
    'BERC Corporate': {
        'background': '#F5F5F5',
        'grid': '#CCCCCC',
        'text': '#1C1C1C',
        'axis': '#1C1C1C',
        'font_family': 'Times New Roman',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'line_colors': [
            '#1F4E78',  # Dark Blue
            '#4472C4',  # Medium Blue
            '#70AD47',  # Green
            '#FFC000',  # Gold
            '#ED7D31',  # Orange
            '#5B9BD5',  # Light Blue
            '#A5A5A5',  # Gray
            '#C55A11',  # Brown
            '#C00000',  # Red
            '#375623',  # Dark Green
        ]
    },
    'Carbon Modern': {
        'background': '#0F1115',
        'grid': '#242A32',
        'text': '#E8EAED',
        'axis': '#9AA0A6',
        'font_family': 'Segoe UI',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'line_colors': [
            '#7C9EFF',  # Soft Indigo
            '#2EC5D3',  # Aqua
            '#F9D162',  # Warm Amber
            '#F37A7A',  # Coral Red
            '#9AE29B',  # Mint
            '#C1C7D0',  # Cool Gray
        ]
    },
    'Nordic Calm': {
        'background': '#F7F9FB',
        'grid': '#D9E2EC',
        'text': '#243B53',
        'axis': '#243B53',
        'font_family': 'Calibri',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'line_colors': [
            '#1F4B99',  # Deep Blue
            '#2D8C9F',  # Teal Blue
            '#5FA777',  # Sage Green
            '#DB8C60',  # Clay
            '#B6598C',  # Mauve Rose
            '#9BA8BC',  # Mist Gray
        ]
    },
    'Sandstone Editorial': {
        'background': '#FFF9F2',
        'grid': '#E7DCC8',
        'text': '#2E2A25',
        'axis': '#3E362E',
        'font_family': 'Georgia',
        'font_size': 11,
        'title_fontsize': 19,
        'title_fontweight': 'bold',
        'line_colors': [
            '#9B5E2A',  # Burnt Umber
            '#CC8B48',  # Sandstone
            '#4F6D7A',  # Slate Blue
            '#7A9E7E',  # Sage
            '#D05B5B',  # Terracotta
            '#A37B73',  # Dusty Rose
        ]
    },
    'Indigo Print': {
        'background': '#FFFFFF',
        'grid': '#DCE2F0',
        'text': '#1B1F3B',
        'axis': '#1B1F3B',
        'font_family': 'Garamond',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'line_colors': [
            '#243B73',  # Indigo
            '#4C6FFF',  # Royal Blue
            '#1D9BF0',  # Azure
            '#E46F61',  # Salmon
            '#F1B24A',  # Saffron
            '#6FB18A',  # Dusty Green
        ]
    },
    'Aurora Tech': {
        'background': '#0B132B',
        'grid': '#1F2A44',
        'text': '#E6EDF7',
        'axis': '#8FA3BF',
        'font_family': 'Roboto',
        'font_size': 11,
        'title_fontsize': 19,
        'title_fontweight': 'bold',
        'line_colors': [
            '#12C2E9',  # Neon Cyan
            '#F64F59',  # Vivid Red
            '#C471ED',  # Vivid Purple
            '#4ADE80',  # Mint Green
            '#FFCE52',  # Soft Gold
            '#7DD3FC',  # Sky Blue
        ]
    },
    'Evergreen Atlas': {
        'background': '#F4F7F4',
        'grid': '#D5DED5',
        'text': '#1F2D2B',
        'axis': '#1F2D2B',
        'font_family': 'Palatino Linotype',
        'font_size': 11,
        'title_fontsize': 19,
        'title_fontweight': 'bold',
        'line_colors': [
            '#2F5D50',  # Deep Evergreen
            '#5B8A72',  # Sage
            '#9BBF98',  # Mint Gray
            '#D0A85C',  # Gold Ochre
            '#A65F46',  # Clay Red
            '#4F709C',  # Steel Blue
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
