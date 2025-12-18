"""Comprehensive style profiles combining themes and layout configurations."""

from typing import Dict, Any


COMPREHENSIVE_STYLES = {
    'IMF Official': {
        'description': 'International Monetary Fund official publication style',
        'background_color': '#FFFFFF',
        'text_color': '#000000',
        'axis_color': '#333333',
        'grid_color': '#D5D5D5',
        'grid_type': 'x_only',
        'grid_alpha': 0.5,
        'grid_style': '--',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
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
    'World Bank Report': {
        'description': 'World Bank publication and report style',
        'background_color': '#FAFAFA',
        'text_color': '#212121',
        'axis_color': '#424242',
        'grid_color': '#D0D0D0',
        'grid_type': 'x_only',
        'grid_alpha': 0.5,
        'grid_style': '--',
        'font_family': 'Garamond',
        'font_size': 10,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'legend_position': 'lower right',
        'legend_ncol': 1,
        'legend_framealpha': 0.85,
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
    'Professional Clean': {
        'description': 'Professional presentation with horizontal gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#333333',
        'grid_color': '#D0D0D0',
        'grid_type': 'x_only',
        'grid_alpha': 0.5,
        'grid_style': '-',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
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
    'Analytical Grid': {
        'description': 'Analytical style with vertical gridlines for value reading',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#333333',
        'grid_color': '#D5D5D5',
        'grid_type': 'y_only',
        'grid_alpha': 0.5,
        'grid_style': ':',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
        'line_colors': [
            '#0063B2',  # Deep Blue
            '#D62728',  # Red
            '#2CA02C',  # Green
            '#FF7F0E',  # Orange
            '#9467BD',  # Purple
            '#8C564B',  # Brown
            '#E377C2',  # Pink
            '#7F7F7F',  # Gray
            '#BCBD22',  # Olive
            '#17BECF',  # Cyan
        ]
    },
    'Academic Journal': {
        'description': 'Academic publication style with serif fonts',
        'background_color': '#FFFFFF',
        'text_color': '#000000',
        'axis_color': '#000000',
        'grid_color': '#E0E0E0',
        'grid_type': 'y_only',
        'grid_alpha': 0.4,
        'grid_style': ':',
        'font_family': 'Times New Roman',
        'font_size': 10,
        'title_fontsize': 14,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.9,
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
    'Presentation': {
        'description': 'Clean presentation style with bold typography',
        'background_color': '#FAFAFA',
        'text_color': '#2C3E50',
        'axis_color': '#2C3E50',
        'grid_color': '#E0E0E0',
        'grid_type': 'x_only',
        'grid_alpha': 0.45,
        'grid_style': '-',
        'font_family': 'Arial',
        'font_size': 12,
        'title_fontsize': 22,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.85,
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
    'Minimal Grid': {
        'description': 'Minimal design with light gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#333333',
        'axis_color': '#666666',
        'grid_color': '#E8E8E8',
        'grid_type': 'x_only',
        'grid_alpha': 0.3,
        'grid_style': ':',
        'font_family': 'Helvetica',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'normal',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.75,
        'line_colors': [
            '#0055B8',  # Bright Blue
            '#C00000',  # Bold Red
            '#70AD47',  # Green
            '#ED7D31',  # Orange
            '#4472C4',  # Medium Blue
            '#5B9BD5',  # Light Blue
            '#C55A11',  # Brown
            '#A5A5A5',  # Gray
            '#375623',  # Dark Green
            '#FFC000',  # Gold
        ]
    },
    'Full Grid': {
        'description': 'Comprehensive gridlines on both axes',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#333333',
        'grid_color': '#CCCCCC',
        'grid_type': 'both',
        'grid_alpha': 0.5,
        'grid_style': '--',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
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
    'No Grid': {
        'description': 'Clean style without gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#333333',
        'grid_color': '#FFFFFF',
        'grid_type': 'none',
        'grid_alpha': 0.0,
        'grid_style': '-',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
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
    'Dark Mode': {
        'description': 'Modern dark theme for reduced eye strain',
        'background_color': '#1E1E1E',
        'text_color': '#FFFFFF',
        'axis_color': '#FFFFFF',
        'grid_color': '#404040',
        'grid_type': 'x_only',
        'grid_alpha': 0.4,
        'grid_style': '-',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.85,
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
    'Economic Data': {
        'description': 'Full grid for detailed economic data analysis',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#2C2C2C',
        'grid_color': '#D5D5D5',
        'grid_type': 'both',
        'grid_alpha': 0.45,
        'grid_style': ':',
        'font_family': 'Arial',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'upper left',
        'legend_ncol': 1,
        'legend_framealpha': 0.9,
        'line_colors': [
            '#003478',  # Deep Blue
            '#C00000',  # Red
            '#70AD47',  # Green
            '#ED7D31',  # Orange
            '#4472C4',  # Medium Blue
            '#A5A5A5',  # Gray
            '#FFC000',  # Gold
            '#5B9BD5',  # Light Blue
            '#375623',  # Dark Green
            '#C55A11',  # Brown
        ]
    },
    'Business Full Grid': {
        'description': 'Professional business style with comprehensive gridlines',
        'background_color': '#F8F8F8',
        'text_color': '#1C1C1C',
        'axis_color': '#2C2C2C',
        'grid_color': '#BDBDBD',
        'grid_type': 'both',
        'grid_alpha': 0.5,
        'grid_style': '--',
        'font_family': 'Calibri',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 2,
        'legend_framealpha': 0.85,
        'line_colors': [
            '#1F4E78',  # Corporate Blue
            '#C00000',  # Corporate Red
            '#70AD47',  # Corporate Green
            '#FFC000',  # Corporate Gold
            '#4472C4',  # Light Blue
            '#ED7D31',  # Orange
            '#A5A5A5',  # Gray
            '#5B9BD5',  # Sky Blue
            '#C55A11',  # Brown
            '#375623',  # Dark Green
        ]
    },
    'Scientific Full Grid': {
        'description': 'Scientific publication with both axis gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#000000',
        'axis_color': '#000000',
        'grid_color': '#CCCCCC',
        'grid_type': 'both',
        'grid_alpha': 0.4,
        'grid_style': '--',
        'font_family': 'Times New Roman',
        'font_size': 9,
        'title_fontsize': 14,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.95,
        'line_colors': [
            '#0063B2',  # Science Blue
            '#DC143C',  # Crimson
            '#00A08A',  # Teal
            '#F2AD00',  # Gold
            '#5BBCD6',  # Sky Blue
            '#F98400',  # Dark Orange
            '#00A896',  # Turquoise
            '#FF6F59',  # Coral
            '#046C9A',  # Ocean Blue
            '#9CC3D5',  # Light Blue
        ]
    },
    'Corporate Light': {
        'description': 'Light corporate style with horizontal gridlines',
        'background_color': '#FAFAFA',
        'text_color': '#2C2C2C',
        'axis_color': '#3E3E3E',
        'grid_color': '#E0E0E0',
        'grid_type': 'x_only',
        'grid_alpha': 0.45,
        'grid_style': '-',
        'font_family': 'Segoe UI',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
        'line_colors': [
            '#0055B8',  # Corporate Blue
            '#E74C3C',  # Corporate Red
            '#27AE60',  # Corporate Green
            '#F39C12',  # Corporate Orange
            '#9B59B6',  # Corporate Purple
            '#1ABC9C',  # Corporate Teal
            '#34495E',  # Corporate Dark
            '#E67E22',  # Burnt Orange
            '#3498DB',  # Light Blue
            '#95A5A6',  # Gray
        ]
    },
    'Data Journalism': {
        'description': 'Modern journalism style with bold colors',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#2C2C2C',
        'grid_color': '#D8D8D8',
        'grid_type': 'x_only',
        'grid_alpha': 0.5,
        'grid_style': '-',
        'font_family': 'Georgia',
        'font_size': 10,
        'title_fontsize': 22,
        'title_fontweight': 'bold',
        'legend_position': 'upper left',
        'legend_ncol': 1,
        'legend_framealpha': 0.85,
        'line_colors': [
            '#E63946',  # Guardian Red
            '#457B9D',  # NYT Blue
            '#2A9D8F',  # WSJ Teal
            '#F4A261',  # FT Orange
            '#264653',  # Economist Navy
            '#E76F51',  # Reuters Orange
            '#8338EC',  # Purple
            '#06AED5',  # Cyan
            '#FF006E',  # Pink
            '#FB5607',  # Bright Orange
        ]
    },
    'Technical Analysis': {
        'description': 'Vertical gridlines for precise value reading',
        'background_color': '#FEFEFE',
        'text_color': '#1A1A1A',
        'axis_color': '#2C2C2C',
        'grid_color': '#D0D0D0',
        'grid_type': 'y_only',
        'grid_alpha': 0.5,
        'grid_style': ':',
        'font_family': 'Arial',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'lower right',
        'legend_ncol': 1,
        'legend_framealpha': 0.85,
        'line_colors': [
            '#2E7D32',  # Trading Green
            '#C62828',  # Trading Red
            '#1565C0',  # Trading Blue
            '#F57C00',  # Trading Orange
            '#6A1B9A',  # Trading Purple
            '#00838F',  # Trading Cyan
            '#558B2F',  # Dark Green
            '#D84315',  # Dark Red
            '#283593',  # Dark Blue
            '#EF6C00',  # Dark Orange
        ]
    },
    'Pastel Soft': {
        'description': 'Soft pastel colors with minimal gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#4A4A4A',
        'axis_color': '#6A6A6A',
        'grid_color': '#E8E8E8',
        'grid_type': 'x_only',
        'grid_alpha': 0.3,
        'grid_style': ':',
        'font_family': 'Calibri',
        'font_size': 11,
        'title_fontsize': 18,
        'title_fontweight': 'normal',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.75,
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
    'Monochrome Print': {
        'description': 'Grayscale for black and white printing',
        'background_color': '#FFFFFF',
        'text_color': '#000000',
        'axis_color': '#000000',
        'grid_color': '#CCCCCC',
        'grid_type': 'y_only',
        'grid_alpha': 0.5,
        'grid_style': '--',
        'font_family': 'Times New Roman',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.9,
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
    'Vibrant Full Grid': {
        'description': 'Bold vibrant colors with full reference grid',
        'background_color': '#FAFAFA',
        'text_color': '#212121',
        'axis_color': '#212121',
        'grid_color': '#D0D0D0',
        'grid_type': 'both',
        'grid_alpha': 0.4,
        'grid_style': ':',
        'font_family': 'Arial',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'legend_position': 'best',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
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
    'Finance Report': {
        'description': 'Financial reporting with conservative colors',
        'background_color': '#FFFFFF',
        'text_color': '#1A1A1A',
        'axis_color': '#2C2C2C',
        'grid_color': '#DADADA',
        'grid_type': 'both',
        'grid_alpha': 0.4,
        'grid_style': '-',
        'font_family': 'Times New Roman',
        'font_size': 10,
        'title_fontsize': 16,
        'title_fontweight': 'bold',
        'legend_position': 'upper left',
        'legend_ncol': 1,
        'legend_framealpha': 0.9,
        'line_colors': [
            '#003B5C',  # Finance Navy
            '#8B0000',  # Finance Dark Red
            '#006400',  # Finance Dark Green
            '#B8860B',  # Finance Dark Gold
            '#191970',  # Finance Midnight Blue
            '#8B4513',  # Finance Saddle Brown
            '#2F4F4F',  # Finance Dark Slate
            '#556B2F',  # Finance Dark Olive
            '#8B008B',  # Finance Dark Magenta
            '#483D8B',  # Finance Dark Slate Blue
        ]
    },
    'Modern Flat': {
        'description': 'Modern flat design with no gridlines',
        'background_color': '#FFFFFF',
        'text_color': '#2C3E50',
        'axis_color': '#34495E',
        'grid_color': '#FFFFFF',
        'grid_type': 'none',
        'grid_alpha': 0.0,
        'grid_style': '-',
        'font_family': 'Segoe UI',
        'font_size': 11,
        'title_fontsize': 20,
        'title_fontweight': 'bold',
        'legend_position': 'upper right',
        'legend_ncol': 1,
        'legend_framealpha': 0.8,
        'line_colors': [
            '#3498DB',  # Flat Blue
            '#E74C3C',  # Flat Red
            '#2ECC71',  # Flat Green
            '#F39C12',  # Flat Orange
            '#9B59B6',  # Flat Purple
            '#1ABC9C',  # Flat Turquoise
            '#E67E22',  # Flat Carrot
            '#95A5A6',  # Flat Silver
            '#34495E',  # Flat Midnight
            '#16A085',  # Flat Green Sea
        ]
    },
}


def get_style(style_name: str) -> Dict[str, Any]:
    """
    Get a comprehensive style by name.
    
    Args:
        style_name: Name of the style
        
    Returns:
        Style dictionary with all settings
        
    Raises:
        ValueError: If style doesn't exist
    """
    if style_name not in COMPREHENSIVE_STYLES:
        available = ', '.join(COMPREHENSIVE_STYLES.keys())
        raise ValueError(f"Style '{style_name}' not found. Available styles: {available}")
    
    return COMPREHENSIVE_STYLES[style_name].copy()


def get_style_names() -> list:
    """
    Get list of available style names.
    
    Returns:
        List of style names
    """
    return list(COMPREHENSIVE_STYLES.keys())
