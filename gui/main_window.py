"""Main window for Excel Chart Generator application."""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
    QTabWidget, QMessageBox, QLabel
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QImage
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import io

from gui.file_panel import FilePanel
from gui.style_panel import StylePanel
from gui.axis_panel import AxisPanel
from gui.export_panel import ExportPanel
from engine.chart_engine import ChartEngine
from engine.config_builder import ChartConfig, LineConfig, AxisConfig, LegendConfig


class ChartPreviewWidget(QWidget):
    """Widget for displaying chart preview."""
    
    def __init__(self, parent=None):
        """Initialize the chart preview widget."""
        super().__init__(parent)
        
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        
    def update_chart(self, figure: Figure):
        """Update the displayed chart."""
        # Replace the canvas with the new figure to preserve all styling
        layout = self.layout()
        if self.canvas is not None:
            layout.removeWidget(self.canvas)
            self.canvas.setParent(None)
        
        self.figure = figure
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.canvas.draw()
        
    def clear(self):
        """Clear the preview."""
        # Show a simple placeholder figure
        placeholder = Figure(figsize=(8, 6), dpi=100)
        ax = placeholder.add_subplot(111)
        ax.text(0.5, 0.5, 'No Preview Available\n\nLoad data and configure chart',
            ha='center', va='center', fontsize=12, color='gray')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        self.update_chart(placeholder)


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        self.chart_engine = ChartEngine()
        self.current_data = None
        self.auto_update = True
        
        self.setWindowTitle("Excel Chart Generator")
        self.setGeometry(100, 100, 1400, 800)
        
        self.setup_ui()
        self.connect_signals()
        
        # Initialize preview
        self.preview_widget.clear()
        
        # Auto-update timer (debounce rapid changes)
        self.update_timer = QTimer()
        self.update_timer.setSingleShot(True)
        self.update_timer.timeout.connect(self.update_preview)
        
    def setup_ui(self):
        """Set up the user interface."""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(5, 5, 5, 5)
        
        # Create tab widget for control panels
        self.tab_widget = QTabWidget()
        
        # File panel
        self.file_panel = FilePanel()
        self.tab_widget.addTab(self.file_panel, "📁 Data")
        
        # Style panel
        self.style_panel = StylePanel()
        self.tab_widget.addTab(self.style_panel, "🎨 Style")
        
        # Axis panel
        self.axis_panel = AxisPanel()
        self.tab_widget.addTab(self.axis_panel, "📊 Axes")
        
        # Export panel
        self.export_panel = ExportPanel()
        self.tab_widget.addTab(self.export_panel, "💾 Export")
        
        left_layout.addWidget(self.tab_widget)
        
        # Right panel - Preview
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(5, 5, 5, 5)
        
        # Preview label
        preview_label = QLabel("Chart Preview")
        preview_label.setStyleSheet("font-size: 14px; font-weight: bold; padding: 5px;")
        right_layout.addWidget(preview_label)
        
        # Chart preview
        self.preview_widget = ChartPreviewWidget()
        right_layout.addWidget(self.preview_widget)
        
        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: gray; font-style: italic; padding: 5px;")
        right_layout.addWidget(self.status_label)
        
        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        
        # Set initial sizes (40% left, 60% right)
        splitter.setSizes([560, 840])
        
        main_layout.addWidget(splitter)
        
        # Status bar
        self.statusBar().showMessage("Ready - Load an Excel file to begin")
        
    def connect_signals(self):
        """Connect signals between components."""
        # File panel signals
        self.file_panel.data_selected.connect(self.on_data_selected)
        
        # Style panel signals
        self.style_panel.style_changed.connect(self.schedule_update)
        
        # Axis panel signals
        self.axis_panel.settings_changed.connect(self.schedule_update)
        
        # Export panel signals
        self.export_panel.export_requested.connect(self.export_chart)
        
    def on_data_selected(self, x_column: str, y1_columns: list, y2_columns: list):
        """
        Handle data selection change.
        
        Args:
            x_column: Selected X column
            y1_columns: List of primary Y columns
            y2_columns: List of secondary Y columns
        """
        # Update line styles in style panel
        from assets.themes import get_theme
        theme = get_theme(self.style_panel.theme_combo.currentText())
        combined_columns = (y1_columns or []) + (y2_columns or [])
        self.style_panel.update_line_styles(combined_columns, theme['line_colors'], y2_columns)
        
        # Set suggested axis labels
        self.axis_panel.set_x_label_suggestion(x_column)
        if len(y1_columns) == 1:
            self.axis_panel.set_y_label_suggestion(y1_columns[0])
        # Suggest Y2 axis label and enable Y2 automatically if a single Y2 column is selected
        if len(y2_columns) == 1:
            # If Y1 not set, leave as-is and set Y2 specifically
            self.axis_panel.set_y2_label_suggestion(y2_columns[0])
        
        # Schedule preview update
        self.schedule_update()
        
    def schedule_update(self):
        """Schedule a preview update (debounced)."""
        if self.auto_update:
            self.update_timer.start(300)  # 300ms debounce
            
    def update_preview(self):
        """Update the chart preview."""
        try:
            # Get plot data
            plot_data = self.file_panel.get_plot_data()
            if not plot_data:
                self.preview_widget.clear()
                self.status_label.setText("No data selected")
                return
            
            self.current_data = plot_data
            
            # Build configuration
            config = self.build_chart_config()
            
            # Generate chart
            figure = self.chart_engine.create_chart(plot_data, config)
            
            # Update preview
            self.preview_widget.update_chart(figure)
            
            self.status_label.setText("✓ Chart updated")
            self.statusBar().showMessage("Preview updated successfully")
            
        except Exception as e:
            self.status_label.setText(f"✗ Error: {str(e)}")
            self.statusBar().showMessage(f"Error: {str(e)}")
            QMessageBox.warning(self, "Preview Error", f"Failed to generate preview:\n{str(e)}")
            
    def build_chart_config(self) -> ChartConfig:
        """
        Build chart configuration from GUI settings.
        
        Returns:
            ChartConfig object
        """
        # Get configurations from panels
        style_config = self.style_panel.get_config()
        axis_config = self.axis_panel.get_config()
        
        # Resolve current theme for axis/text colors
        from assets.themes import get_theme
        theme = get_theme(self.style_panel.theme_combo.currentText())

        # Create axis configurations
        x_axis = AxisConfig(
            label=axis_config['x_axis']['label'],
            min_value=axis_config['x_axis']['min_value'],
            max_value=axis_config['x_axis']['max_value'],
            tick_rotation=axis_config['x_axis']['tick_rotation'],
            color=theme.get('axis', '#000000'),
            label_fontweight=axis_config['x_axis'].get('label_fontweight', 'normal'),
            grid=style_config['show_grid'],
            grid_color=style_config['grid_color'],
            scale=axis_config['x_axis']['scale'],
            value_format=axis_config['x_axis']['value_format'],
            tick_step=axis_config['x_axis']['tick_step'],
            categorical=axis_config['x_axis']['categorical'],
            hide_labels=axis_config['x_axis']['hide_labels'],
            grouped_categorical=axis_config['x_axis']['grouped_categorical']
        )
        
        y_axis = AxisConfig(
            label=axis_config['y_axis']['label'],
            min_value=axis_config['y_axis']['min_value'],
            max_value=axis_config['y_axis']['max_value'],
            tick_rotation=axis_config['y_axis']['tick_rotation'],
            color=theme.get('axis', '#000000'),
            label_fontweight=axis_config['y_axis'].get('label_fontweight', 'normal'),
            grid=style_config['show_grid'],
            grid_color=style_config['grid_color'],
            scale=axis_config['y_axis']['scale'],
            value_format=axis_config['y_axis']['value_format'],
            tick_step=axis_config['y_axis']['tick_step'],
            categorical=axis_config['y_axis']['categorical'],
            hide_labels=axis_config['y_axis']['hide_labels'],
            grouped_categorical=axis_config['y_axis']['grouped_categorical']
        )
        
        # Determine if y2_axis should be created (check if any line uses secondary axis OR if enable_y2_check is checked)
        has_secondary_lines = any(line_data.get('use_secondary_axis', False) for line_data in style_config['line_configs'])
        
        y2_axis = None
        if axis_config['y2_axis'] or has_secondary_lines:
            # Use existing y2_axis config if available, otherwise create a default one
            y2_config = axis_config['y2_axis'] if axis_config['y2_axis'] else {}
            y2_axis = AxisConfig(
                label=y2_config.get('label', ''),
                min_value=y2_config.get('min_value'),
                max_value=y2_config.get('max_value'),
                tick_rotation=y2_config.get('tick_rotation', 0),
                color=theme.get('axis', '#000000'),
                label_fontweight=y2_config.get('label_fontweight', 'normal'),
                grid=False,  # Don't show grid for secondary axis
                scale=y2_config.get('scale', 'linear'),
                value_format=y2_config.get('value_format', 'auto'),
                tick_step=y2_config.get('tick_step', 0),
                categorical=y2_config.get('categorical', False),
                hide_labels=y2_config.get('hide_labels', False),
                grouped_categorical=y2_config.get('grouped_categorical', False)
            )
        
        # Create line configurations
        lines = []
        for line_data in style_config['line_configs']:
            line = LineConfig(
                column=line_data['column'],
                label=line_data['column'],
                color=line_data['color'],
                style=line_data['style'],
                width=line_data['width'],
                marker=line_data['marker'],
                marker_size=6.0,
                use_secondary_axis=line_data['use_secondary_axis'],
                smoothing_method=line_data.get('smoothing_method', 'none'),
                smoothing_window=line_data.get('smoothing_window', 1)
            )
            lines.append(line)
        
        # Create legend configuration
        legend = LegendConfig(
            show=style_config['show_legend'],
            location=style_config['legend_position'],
            title=style_config['legend_title'],
            ncol=style_config['legend_ncol'],
            framealpha=style_config['legend_framealpha'],
            labelspacing=style_config['legend_labelspacing'],
            handlelength=style_config['legend_handlelength'],
            handletextpad=style_config['legend_handletextpad']
        )
        
        # Get X column
        x_column, _, _ = self.file_panel.get_selected_data()
        
        # Get period highlights from special presets
        special_config = self.style_panel.get_special_preset_config()
        period_highlights = []
        for ph_data in special_config.get('period_highlights', []):
            from engine.config_builder import PeriodHighlight
            ph = PeriodHighlight(
                name=ph_data.get('name', ''),
                start=ph_data.get('start'),
                end=ph_data.get('end'),
                color=ph_data.get('color', '#FF0000'),
                alpha=ph_data.get('alpha', 0.1),
                label=ph_data.get('label', '')
            )
            period_highlights.append(ph)
        
        # Create complete configuration
        config = ChartConfig(
            title=axis_config['title'],
            title_fontsize=style_config['title_fontsize'],
            title_loc=axis_config.get('title_loc', 'center'),
            title_yoffset=axis_config.get('title_yoffset', 1.0),
            subtitle=axis_config.get('subtitle', ''),
            subtitle_fontsize=axis_config.get('subtitle_fontsize', 12),
            subtitle_fontweight=axis_config.get('subtitle_fontweight', 'normal'),
            subtitle_loc=axis_config.get('subtitle_loc', 'center'),
            subtitle_yoffset=axis_config.get('subtitle_yoffset', 0.94),
            x_column=x_column or '',
            lines=lines,
            x_axis=x_axis,
            y_axis=y_axis,
            y2_axis=y2_axis,
            background_color=style_config['background_color'],
            font_family=style_config['font_family'],
            font_size=style_config['font_size'],
            text_color=theme.get('text', '#000000'),
            legend=legend,
            figure_width=axis_config['figure_width'],
            figure_height=axis_config['figure_height'],
            period_highlights=period_highlights
        )
        
        return config
        
    def export_chart(self, output_path: str, format: str, dpi: int):
        """
        Export the chart to a file.
        
        Args:
            output_path: Path to save the file
            format: Output format (png, svg, pdf)
            dpi: DPI for raster formats
        """
        try:
            # Ensure we have current data
            if self.current_data is None:
                raise ValueError("No chart data available. Please configure a chart first.")
            
            # Build fresh configuration
            config = self.build_chart_config()
            
            # Generate chart with export DPI
            config.dpi = dpi
            figure = self.chart_engine.create_chart(self.current_data, config)
            
            # Save chart
            self.chart_engine.save_chart(output_path, format, dpi)
            
            # Show success
            self.export_panel.set_export_success(output_path)
            self.statusBar().showMessage(f"Chart exported successfully to {output_path}")
            
            QMessageBox.information(
                self,
                "Export Successful",
                f"Chart has been exported to:\n{output_path}"
            )
            
        except Exception as e:
            self.export_panel.set_export_error(str(e))
            self.statusBar().showMessage(f"Export failed: {str(e)}")
            QMessageBox.critical(
                self,
                "Export Error",
                f"Failed to export chart:\n{str(e)}"
            )
            
    def closeEvent(self, event):
        """Handle window close event."""
        # Clean up
        self.chart_engine.clear()
        event.accept()
