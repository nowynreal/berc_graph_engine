"""Matplotlib-based chart rendering engine."""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib import ticker
from matplotlib import font_manager as fm
import pandas as pd
from typing import Dict, Optional
from pathlib import Path

from .config_builder import ChartConfig


class ChartEngine:
    """Handles chart generation using matplotlib."""
    
    def __init__(self):
        """Initialize the chart engine."""
        self.figure: Optional[Figure] = None
        self.config: Optional[ChartConfig] = None
        
    def create_chart(self, data: Dict[str, pd.Series], config: ChartConfig) -> Figure:
        """
        Create a chart from data and configuration.
        
        Args:
            data: Dictionary with 'x' key and column names as keys
            config: Chart configuration
            
        Returns:
            Matplotlib Figure object
            
        Raises:
            ValueError: If data or configuration is invalid
        """
        # Validate inputs
        if not data:
            raise ValueError("No data provided")
        if 'x' not in data:
            raise ValueError("Data must contain 'x' key")
        if not config.lines:
            raise ValueError("No lines configured")
        
        # Store configuration
        self.config = config
        
        # Create figure and primary axis
        self.figure = plt.figure(
            figsize=(config.figure_width, config.figure_height),
            dpi=config.dpi,
            facecolor=config.background_color
        )
        
        ax1 = self.figure.add_subplot(111)
        ax1.set_facecolor(config.background_color)
        
        # Set font and text properties (with robust fallback)
        requested_family = config.font_family
        resolved_family = requested_family
        try:
            fm.findfont(requested_family, fallback_to_default=False)
        except Exception:
            for fb in ['Segoe UI', 'Arial', 'Calibri', 'DejaVu Sans', 'sans-serif']:
                try:
                    fm.findfont(fb, fallback_to_default=False)
                    resolved_family = fb
                    break
                except Exception:
                    continue
        plt.rcParams['font.family'] = resolved_family
        plt.rcParams['font.size'] = config.font_size
        plt.rcParams['text.color'] = getattr(config, 'text_color', '#000000')
        
        # Prepare X data (categorical or numeric)
        x_labels = None
        if config.x_axis.categorical:
            x_labels = list(data['x'])
            x_values = list(range(len(x_labels)))
        else:
            x_values = data['x']

        # Plot primary Y-axis lines
        primary_lines = config.get_primary_lines()
        for line_config in primary_lines:
            if line_config.column not in data:
                continue

            # Prepare series (apply smoothing if requested)
            y_values = data[line_config.column]
            y_values = self._apply_smoothing(y_values, line_config)

            ax1.plot(
                x_values,
                y_values,
                label=line_config.label,
                color=line_config.color,
                linestyle=line_config.style,
                linewidth=line_config.width,
                marker=line_config.marker if line_config.marker else None,
                markersize=line_config.marker_size,
                markerfacecolor=line_config.color,
                markeredgecolor=line_config.color,
                solid_capstyle='round',
                solid_joinstyle='round',
                dash_joinstyle='round',
                antialiased=True
            )
        
        # Configure primary Y-axis
        self._configure_axis(ax1, config.y_axis, is_y_axis=True)
        
        # Create secondary Y-axis if enabled
        ax2 = None
        if config.y2_axis is not None:
            ax2 = ax1.twinx()
            
            # Plot lines assigned to secondary Y-axis
            secondary_lines = config.get_secondary_lines()
            for line_config in secondary_lines:
                if line_config.column not in data:
                    continue

                # Prepare series (apply smoothing if requested)
                y2_values = data[line_config.column]
                y2_values = self._apply_smoothing(y2_values, line_config)

                ax2.plot(
                    x_values,
                    y2_values,
                    label=line_config.label,
                    color=line_config.color,
                    linestyle=line_config.style,
                    linewidth=line_config.width,
                    marker=line_config.marker if line_config.marker else None,
                    markersize=line_config.marker_size,
                    markerfacecolor=line_config.color,
                    markeredgecolor=line_config.color,
                    solid_capstyle='round',
                    solid_joinstyle='round',
                    dash_joinstyle='round',
                    antialiased=True
                )
            
            # Configure secondary Y-axis
            self._configure_axis(ax2, config.y2_axis, is_y_axis=True)
        
        # Configure X-axis (pass labels if categorical)
        self._configure_axis(ax1, config.x_axis, is_y_axis=False, labels=x_labels)
        
        # Helper to map a period boundary to the plotted x-axis
        def _resolve_period_position(value):
            if value is None:
                return None
            if x_labels:
                # Try numeric match first, then string match, fallback to bounds
                for idx, label in enumerate(x_labels):
                    try:
                        if isinstance(label, (int, float)) and float(value) == float(label):
                            return idx
                    except (ValueError, TypeError):
                        pass
                    if str(label) == str(value):
                        return idx
                return len(x_labels) - 1 if value is not None else 0
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

        # Apply period highlights (background shading)
        for period in config.period_highlights:
            if period.start is not None and period.end is not None:
                try:
                    start_val = _resolve_period_position(period.start)
                    end_val = _resolve_period_position(period.end)
                    if start_val is None or end_val is None:
                        continue

                    ax1.axvspan(start_val, end_val, alpha=period.alpha, color=period.color, zorder=0)
                    if period.label:
                        mid = (start_val + end_val) / 2
                        y_pos = ax1.get_ylim()[1] * 0.95
                        ax1.text(mid, y_pos, period.label, ha='center', va='top', 
                                fontsize=9, color=period.color, alpha=0.6, style='italic')
                except (ValueError, TypeError):
                    # Skip invalid period
                    pass
        
        # Set title with alignment, offset, and theme text color
        ax1.set_title(
            config.title,
            fontsize=config.title_fontsize,
            fontweight=config.title_fontweight,
            color=getattr(config, 'text_color', config.y_axis.color),
            loc=config.title_loc,
            y=config.title_yoffset
        )

        # Optional subtitle with flexible positioning
        if getattr(config, 'subtitle', ''):
            subtitle_loc = getattr(config, 'subtitle_loc', 'chart_center')
            sub_y = config.title_yoffset + getattr(config, 'subtitle_yoffset', -0.06)
            
            # Parse location mode
            if subtitle_loc.startswith('figure_'):
                # Figure-based alignment (entire canvas)
                align = subtitle_loc.replace('figure_', '')
                sub_x = 0.0 if align == 'left' else 1.0
                sub_ha = 'left' if align == 'left' else 'right'
                self.figure.text(
                    sub_x, sub_y,
                    config.subtitle,
                    fontsize=getattr(config, 'subtitle_fontsize', 12),
                    fontweight=getattr(config, 'subtitle_fontweight', 'normal'),
                    color=getattr(config, 'text_color', config.y_axis.color),
                    ha=sub_ha, va='top'
                )
            else:
                # Chart-based alignment (axes area) - default
                align = subtitle_loc.replace('chart_', '') if subtitle_loc.startswith('chart_') else subtitle_loc
                if align == 'left':
                    sub_x, sub_ha = 0.0, 'left'
                elif align == 'right':
                    sub_x, sub_ha = 1.0, 'right'
                else:
                    sub_x, sub_ha = 0.5, 'center'
                ax1.text(
                    sub_x, sub_y,
                    config.subtitle,
                    fontsize=getattr(config, 'subtitle_fontsize', 12),
                    fontweight=getattr(config, 'subtitle_fontweight', 'normal'),
                    color=getattr(config, 'text_color', config.y_axis.color),
                    ha=sub_ha, va='top',
                    transform=ax1.transAxes
                )
        
        # Configure legend
        if config.legend.show:
            handles1, labels1 = ax1.get_legend_handles_labels()
            
            if ax2 is not None:
                handles2, labels2 = ax2.get_legend_handles_labels()
                handles = handles1 + handles2
                labels = labels1 + labels2
            else:
                handles = handles1
                labels = labels1
            
            if handles:
                lgd = ax1.legend(
                    handles,
                    labels,
                    loc=config.legend.location,
                    frameon=config.legend.frameon,
                    shadow=config.legend.shadow,
                    ncol=config.legend.ncol,
                    fontsize=config.legend.fontsize,
                    framealpha=getattr(config.legend, 'framealpha', 0.8),
                    labelspacing=getattr(config.legend, 'labelspacing', 0.5),
                    handlelength=getattr(config.legend, 'handlelength', 2.0),
                    handletextpad=getattr(config.legend, 'handletextpad', 0.8)
                )
                if getattr(config.legend, 'title', ''):
                    lgd.set_title(config.legend.title)
        
        # Apply tight layout
        if config.tight_layout:
            self.figure.tight_layout()
        
        return self.figure

    def _apply_smoothing(self, series, line_config):
        """Apply smoothing to a series if requested (returns list/Series)."""
        method = getattr(line_config, 'smoothing_method', 'none')
        window = max(1, int(getattr(line_config, 'smoothing_window', 1)))
        if method == 'moving_average' and window > 1:
            try:
                s = pd.Series(series)
                sm = s.rolling(window=window, center=True, min_periods=1).mean()
                return sm.tolist()
            except Exception:
                # Fallback simple moving average without pandas if needed
                vals = list(series)
                n = len(vals)
                out = []
                half = window // 2
                for i in range(n):
                    start = max(0, i - half)
                    end = min(n, i + half + 1)
                    out.append(sum(vals[start:end]) / (end - start))
                return out
        return series
    
    def _configure_axis(self, ax, axis_config, is_y_axis: bool, labels=None):
        """
        Configure an axis with the provided settings.
        
        Args:
            ax: Matplotlib axis object
            axis_config: AxisConfig object
            is_y_axis: True if configuring Y-axis, False for X-axis
        """
        # Set label
        if is_y_axis:
            ax.set_ylabel(axis_config.label, color=axis_config.color, fontweight=getattr(axis_config, 'label_fontweight', 'normal'))
        else:
            ax.set_xlabel(axis_config.label, color=axis_config.color, fontweight=getattr(axis_config, 'label_fontweight', 'normal'))
        
        # Set axis color
        ax.tick_params(axis='y' if is_y_axis else 'x', colors=axis_config.color)
        
        # Set spine color
        if is_y_axis:
            # For Y-axis, set both left and right spines (for twinx support)
            ax.spines['left'].set_color(axis_config.color)
            ax.spines['right'].set_color(axis_config.color)
        else:
            ax.spines['bottom'].set_color(axis_config.color)
            # Also color the top spine for consistency in dark themes
            if 'top' in ax.spines:
                ax.spines['top'].set_color(axis_config.color)

        # Scale
        if axis_config.scale == 'log':
            if is_y_axis:
                ax.set_yscale('log')
            else:
                ax.set_xscale('log')
        else:
            if is_y_axis:
                ax.set_yscale('linear')
            else:
                ax.set_xscale('linear')
        
        # Set limits
        if is_y_axis:
            if axis_config.min_value is not None or axis_config.max_value is not None:
                ax.set_ylim(axis_config.min_value, axis_config.max_value)
        else:
            if axis_config.min_value is not None or axis_config.max_value is not None:
                ax.set_xlim(axis_config.min_value, axis_config.max_value)
        
        # Set tick rotation
        if axis_config.tick_rotation != 0:
            if is_y_axis:
                ax.tick_params(axis='y', rotation=axis_config.tick_rotation)
            else:
                ax.tick_params(axis='x', rotation=axis_config.tick_rotation)
        
        # Configure grid
        if axis_config.grid:
            ax.grid(
                True,
                axis='y' if is_y_axis else 'x',
                color=axis_config.grid_color,
                alpha=axis_config.grid_alpha,
                linestyle=axis_config.grid_style
            )

        # Format ticks
        # Format ticks
        fmt = axis_config.value_format
        if fmt == 'percent':
            ax.yaxis.set_major_formatter(ticker.PercentFormatter()) if is_y_axis else ax.xaxis.set_major_formatter(ticker.PercentFormatter())
        elif fmt == 'scientific':
            sf = ticker.ScalarFormatter(useMathText=True)
            sf.set_scientific(True)
            (ax.yaxis if is_y_axis else ax.xaxis).set_major_formatter(sf)
        elif fmt == 'integer':
            (ax.yaxis if is_y_axis else ax.xaxis).set_major_locator(ticker.MaxNLocator(integer=True))
        elif fmt == 'decimal':
            (ax.yaxis if is_y_axis else ax.xaxis).set_major_formatter(ticker.FormatStrFormatter('%.2f'))

        # Tick step (numeric axes only; skip for categorical labels)
        if axis_config.tick_step and not (labels is not None and not is_y_axis):
            locator = ticker.MultipleLocator(axis_config.tick_step)
            (ax.yaxis if is_y_axis else ax.xaxis).set_major_locator(locator)

        # Apply categorical labels for X if provided
        if labels is not None and not is_y_axis:
            positions = list(range(len(labels)))
            
            if axis_config.grouped_categorical:
                # Extract year groups from labels like "2006 q1", "2006 q2", etc.
                groups = []
                group_positions = []
                current_group = None
                
                for i, label in enumerate(labels):
                    # Extract group prefix (text before first space)
                    parts = str(label).split(None, 1)
                    group = parts[0] if parts else str(label)
                    
                    if group != current_group:
                        groups.append(group)
                        group_positions.append(i)
                        current_group = group
                
                # Set minor ticks at all positions (for grid lines)
                ax.set_xticks(positions, minor=True)
                ax.tick_params(axis='x', which='minor', length=4, grid_alpha=0.3)
                
                # Set major ticks only at group boundaries
                ax.set_xticks(group_positions)
                ax.set_xticklabels(groups, rotation=axis_config.tick_rotation)
                for lab in ax.get_xticklabels():
                    lab.set_color(axis_config.color)
                
                # Enable minor grid if main grid is on
                if axis_config.grid:
                    ax.grid(True, axis='x', which='minor', color=axis_config.grid_color, 
                           alpha=axis_config.grid_alpha * 0.5, linestyle=':')
            else:
                ax.set_xticks(positions)
                if axis_config.hide_labels:
                    ax.tick_params(axis='x', labelbottom=False)
                else:
                    ax.set_xticklabels(labels, rotation=axis_config.tick_rotation)
                    for lab in ax.get_xticklabels():
                        lab.set_color(axis_config.color)

        # Hide labels but keep ticks/grid for numeric axes when requested
        if axis_config.hide_labels and labels is None:
            if is_y_axis:
                ax.tick_params(axis='y', labelleft=False, labelright=False)
            else:
                ax.tick_params(axis='x', labelbottom=False)
    
    def save_chart(self, output_path: str, format: str = 'png', dpi: Optional[int] = None):
        """
        Save the chart to a file.
        
        Args:
            output_path: Path where to save the file
            format: Output format (png, svg, pdf)
            dpi: DPI for raster formats (uses config DPI if not specified)
            
        Raises:
            ValueError: If no chart has been created or invalid format
        """
        if self.figure is None:
            raise ValueError("No chart created. Call create_chart() first.")
        
        format = format.lower()
        valid_formats = ['png', 'svg', 'pdf']
        if format not in valid_formats:
            raise ValueError(f"Invalid format: {format}. Must be one of {valid_formats}")
        
        # Ensure output directory exists
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Use config DPI if not specified
        save_dpi = dpi if dpi is not None else (self.config.dpi if self.config else 100)
        
        # Save the figure
        self.figure.savefig(
            output_path,
            format=format,
            dpi=save_dpi if format == 'png' else None,
            bbox_inches='tight',
            facecolor=self.figure.get_facecolor(),
            edgecolor='none'
        )
    
    def get_figure(self) -> Optional[Figure]:
        """
        Get the current figure.
        
        Returns:
            Current matplotlib Figure or None
        """
        return self.figure
    
    def clear(self):
        """Clear the current figure and reset state."""
        if self.figure is not None:
            plt.close(self.figure)
            self.figure = None
        self.config = None
