"""Configuration builder for chart settings."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class PeriodHighlight:
    """Highlight a time period on the chart."""
    name: str = "Period"
    start: Optional[float] = None  # x-axis value or index
    end: Optional[float] = None
    color: str = "#FF0000"
    alpha: float = 0.1
    label: str = ""


@dataclass
class AxisConfig:
    """Configuration for a chart axis."""
    label: str = ""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    tick_rotation: int = 0
    color: str = "#000000"
    label_fontweight: str = 'normal'   # 'normal' or 'bold'
    grid: bool = True
    grid_type: str = 'y_only'  # 'both', 'x_only', 'y_only', 'none' - applies to primary grid axis
    grid_color: str = "#CCCCCC"
    grid_alpha: float = 0.5
    grid_style: str = '--'
    scale: str = 'linear'          # 'linear' or 'log'
    value_format: str = 'auto'     # 'auto', 'decimal', 'scientific', 'percent', 'integer'
    tick_step: Optional[float] = None  # custom major tick interval
    categorical: bool = False          # treat axis as categorical (preserve order/labels)
    hide_labels: bool = False          # keep ticks/grid but suppress tick labels
    grouped_categorical: bool = False  # group labels by prefix (e.g., '2006 q1' -> show only '2006')


@dataclass
class LineConfig:
    """Configuration for a single line in the chart."""
    column: str
    label: str = ""
    color: str = "#1f77b4"
    style: str = '-'
    width: float = 2.0
    marker: str = ''
    marker_size: float = 6.0
    use_secondary_axis: bool = False
    smoothing_method: str = 'none'   # 'none' or 'moving_average'
    smoothing_window: int = 1
    
    def __post_init__(self):
        """Set default label if not provided."""
        if not self.label:
            self.label = self.column


@dataclass
class LegendConfig:
    """Configuration for chart legend."""
    show: bool = True
    location: str = 'best'
    frameon: bool = True
    shadow: bool = False
    ncol: int = 1
    fontsize: int = 10
    title: str = ''
    framealpha: float = 0.8
    fancybox: bool = True
    labelspacing: float = 0.5
    handlelength: float = 2.0
    handletextpad: float = 0.8


@dataclass
class ChartConfig:
    """Complete configuration for chart generation."""
    
    # Title
    title: str = "Chart"
    title_fontsize: int = 16
    title_fontweight: str = 'bold'
    title_loc: str = 'center'          # 'left', 'center', 'right'
    title_yoffset: float = 1.0         # relative position
    subtitle: str = ''
    subtitle_fontsize: int = 12
    subtitle_fontweight: str = 'normal'
    subtitle_loc: str = 'center'       # 'left', 'center', 'right'
    subtitle_yoffset: float = 0.94
    
    # Data columns
    x_column: str = ""
    lines: List[LineConfig] = field(default_factory=list)
    
    # Axes
    x_axis: AxisConfig = field(default_factory=AxisConfig)
    y_axis: AxisConfig = field(default_factory=AxisConfig)
    y2_axis: Optional[AxisConfig] = None
    
    # Style
    background_color: str = "#FFFFFF"
    font_family: str = "sans-serif"
    font_size: int = 10
    text_color: str = "#000000"
    
    # Legend
    legend: LegendConfig = field(default_factory=LegendConfig)
    
    # Period highlights (for time range shading, annotations)
    period_highlights: List[PeriodHighlight] = field(default_factory=list)
    
    # Figure
    figure_width: float = 10.0
    figure_height: float = 6.0
    dpi: int = 100
    tight_layout: bool = True
    
    def has_secondary_axis(self) -> bool:
        """Check if any line uses the secondary Y-axis."""
        return any(line.use_secondary_axis for line in self.lines)
    
    def get_primary_lines(self) -> List[LineConfig]:
        """Get lines for primary Y-axis."""
        return [line for line in self.lines if not line.use_secondary_axis]
    
    def get_secondary_lines(self) -> List[LineConfig]:
        """Get lines for secondary Y-axis."""
        return [line for line in self.lines if line.use_secondary_axis]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            'title': self.title,
            'title_fontsize': self.title_fontsize,
            'title_fontweight': self.title_fontweight,
            'title_loc': self.title_loc,
            'title_yoffset': self.title_yoffset,
            'subtitle': self.subtitle,
            'subtitle_fontsize': self.subtitle_fontsize,
            'subtitle_fontweight': self.subtitle_fontweight,
            'subtitle_loc': self.subtitle_loc,
            'subtitle_yoffset': self.subtitle_yoffset,
            'x_column': self.x_column,
            'lines': [
                {
                    'column': line.column,
                    'label': line.label,
                    'color': line.color,
                    'style': line.style,
                    'width': line.width,
                    'marker': line.marker,
                    'marker_size': line.marker_size,
                    'use_secondary_axis': line.use_secondary_axis,
                    'smoothing_method': line.smoothing_method,
                    'smoothing_window': line.smoothing_window
                }
                for line in self.lines
            ],
            'x_axis': {
                'label': self.x_axis.label,
                'min_value': self.x_axis.min_value,
                'max_value': self.x_axis.max_value,
                'tick_rotation': self.x_axis.tick_rotation,
                'color': self.x_axis.color,
                'label_fontweight': self.x_axis.label_fontweight,
                'grid': self.x_axis.grid,
                'grid_type': self.x_axis.grid_type,
                'grid_color': self.x_axis.grid_color,
                'grid_alpha': self.x_axis.grid_alpha,
                'grid_style': self.x_axis.grid_style,
                'scale': self.x_axis.scale,
                'value_format': self.x_axis.value_format,
                'tick_step': self.x_axis.tick_step,
                'categorical': self.x_axis.categorical,
                'hide_labels': self.x_axis.hide_labels,
                'grouped_categorical': self.x_axis.grouped_categorical
            },
            'y_axis': {
                'label': self.y_axis.label,
                'min_value': self.y_axis.min_value,
                'max_value': self.y_axis.max_value,
                'tick_rotation': self.y_axis.tick_rotation,
                'color': self.y_axis.color,
                'label_fontweight': self.y_axis.label_fontweight,
                'grid': self.y_axis.grid,
                'grid_type': self.y_axis.grid_type,
                'grid_color': self.y_axis.grid_color,
                'grid_alpha': self.y_axis.grid_alpha,
                'grid_style': self.y_axis.grid_style,
                'scale': self.y_axis.scale,
                'value_format': self.y_axis.value_format,
                'tick_step': self.y_axis.tick_step,
                'categorical': self.y_axis.categorical,
                'hide_labels': self.y_axis.hide_labels,
                'grouped_categorical': self.y_axis.grouped_categorical
            },
            'y2_axis': {
                'label': self.y2_axis.label,
                'min_value': self.y2_axis.min_value,
                'max_value': self.y2_axis.max_value,
                'tick_rotation': self.y2_axis.tick_rotation,
                'color': self.y2_axis.color,
                'label_fontweight': self.y2_axis.label_fontweight,
                'grid': self.y2_axis.grid,
                'grid_type': self.y2_axis.grid_type,
                'grid_color': self.y2_axis.grid_color,
                'grid_alpha': self.y2_axis.grid_alpha,
                'grid_style': self.y2_axis.grid_style,
                'scale': self.y2_axis.scale,
                'value_format': self.y2_axis.value_format,
                'tick_step': self.y2_axis.tick_step,
                'categorical': self.y2_axis.categorical,
                'hide_labels': self.y2_axis.hide_labels,
                'grouped_categorical': self.y2_axis.grouped_categorical
            } if self.y2_axis else None,
            'background_color': self.background_color,
            'font_family': self.font_family,
            'font_size': self.font_size,
            'text_color': self.text_color,
            'legend': {
                'show': self.legend.show,
                'location': self.legend.location,
                'frameon': self.legend.frameon,
                'shadow': self.legend.shadow,
                'ncol': self.legend.ncol,
                'fontsize': self.legend.fontsize,
                'title': self.legend.title,
                'framealpha': self.legend.framealpha,
                'fancybox': self.legend.fancybox,
                'labelspacing': self.legend.labelspacing,
                'handlelength': self.legend.handlelength,
                'handletextpad': self.legend.handletextpad
            },
            'figure_width': self.figure_width,
            'figure_height': self.figure_height,
            'dpi': self.dpi,
            'tight_layout': self.tight_layout
        }
