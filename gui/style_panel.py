"""Style configuration panel for chart appearance."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QSpinBox, QDoubleSpinBox, QPushButton, QGroupBox, QCheckBox,
    QColorDialog, QScrollArea, QFrame, QLineEdit, QTabWidget
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QColor

from assets.themes import get_theme_names


class ColorButton(QPushButton):
    """Button that displays and allows selecting a color."""
    
    color_changed = Signal(str)
    
    def __init__(self, initial_color: str = "#000000", parent=None):
        """Initialize the color button."""
        super().__init__(parent)
        
        self.current_color = initial_color
        self.setFixedSize(80, 25)
        self.update_color(initial_color)
        self.clicked.connect(self.choose_color)
        
    def update_color(self, color: str):
        """Update button color."""
        self.current_color = color
        self.setStyleSheet(f"background-color: {color}; border: 1px solid #888;")
        
    def choose_color(self):
        """Open color picker dialog."""
        color = QColorDialog.getColor(QColor(self.current_color), self)
        if color.isValid():
            self.update_color(color.name())
            self.color_changed.emit(color.name())
            
    def get_color(self) -> str:
        """Get current color."""
        return self.current_color


class LineStyleWidget(QWidget):
    """Widget for configuring a single line's style."""
    
    style_changed = Signal()
    
    def __init__(self, column_name: str, color: str = "#1f77b4", parent=None):
        """Initialize the line style widget."""
        super().__init__(parent)
        
        self.column_name = column_name
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 2, 0, 2)
        
        # Column label
        label = QLabel(column_name)
        label.setMinimumWidth(100)
        layout.addWidget(label)
        
        # Color picker
        self.color_button = ColorButton(color)
        self.color_button.color_changed.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.color_button)
        
        # Line style
        self.style_combo = QComboBox()
        self.style_combo.addItems(['─ Solid', '-- Dashed', '·· Dotted', '-· Dash-Dot'])
        self.style_combo.setItemData(0, '-')
        self.style_combo.setItemData(1, '--')
        self.style_combo.setItemData(2, ':')
        self.style_combo.setItemData(3, '-.')
        self.style_combo.currentIndexChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.style_combo)
        
        # Line width
        self.width_spin = QDoubleSpinBox()
        self.width_spin.setRange(0.5, 10.0)
        self.width_spin.setValue(2.0)
        self.width_spin.setSingleStep(0.5)
        self.width_spin.setPrefix("Width: ")
        self.width_spin.valueChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.width_spin)
        
        # Marker style
        self.marker_combo = QComboBox()
        self.marker_combo.addItems(['None', '● Circle', '■ Square', '▲ Triangle', '◆ Diamond', '+ Plus', '✕ Cross'])
        self.marker_combo.setItemData(0, '')
        self.marker_combo.setItemData(1, 'o')
        self.marker_combo.setItemData(2, 's')
        self.marker_combo.setItemData(3, '^')
        self.marker_combo.setItemData(4, 'D')
        self.marker_combo.setItemData(5, '+')
        self.marker_combo.setItemData(6, 'x')
        self.marker_combo.currentIndexChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.marker_combo)
        
        # Secondary axis checkbox
        self.secondary_check = QCheckBox("Y2")
        self.secondary_check.setToolTip("Use secondary Y-axis")
        self.secondary_check.stateChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.secondary_check)

        # Smoothing method
        self.smooth_combo = QComboBox()
        self.smooth_combo.addItems(['No Smooth', 'Moving Avg'])
        self.smooth_combo.setItemData(0, 'none')
        self.smooth_combo.setItemData(1, 'moving_average')
        self.smooth_combo.currentIndexChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.smooth_combo)

        # Smoothing window
        self.smooth_window_spin = QSpinBox()
        self.smooth_window_spin.setRange(1, 25)
        self.smooth_window_spin.setValue(3)
        self.smooth_window_spin.setPrefix("Win: ")
        self.smooth_window_spin.valueChanged.connect(lambda: self.style_changed.emit())
        layout.addWidget(self.smooth_window_spin)
        
        layout.addStretch()
        
    def get_config(self) -> dict:
        """Get line configuration."""
        return {
            'column': self.column_name,
            'color': self.color_button.get_color(),
            'style': self.style_combo.currentData(),
            'width': self.width_spin.value(),
            'marker': self.marker_combo.currentData(),
            'use_secondary_axis': self.secondary_check.isChecked(),
            'smoothing_method': self.smooth_combo.currentData(),
            'smoothing_window': self.smooth_window_spin.value()
        }
        
    def set_color(self, color: str):
        """Set line color."""
        self.color_button.update_color(color)


class StylePanel(QWidget):
    """Panel for configuring chart style and appearance."""
    
    style_changed = Signal()
    
    def __init__(self, parent=None):
        """Initialize the style panel."""
        super().__init__(parent)
        
        self.line_widgets = {}
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        tab = QTabWidget()
        main_layout.addWidget(tab)

        # --- General tab ---
        general_tab = QWidget()
        general_layout = QVBoxLayout(general_tab)
        general_layout.setSpacing(8)

        theme_group = QGroupBox("Theme")
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Preset:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(get_theme_names())
        self.theme_combo.currentTextChanged.connect(self.apply_theme)
        theme_layout.addWidget(self.theme_combo, 1)
        theme_group.setLayout(theme_layout)
        general_layout.addWidget(theme_group)

        # Special presets (COVID, Recession, etc.)
        special_group = QGroupBox("Special Scenarios")
        special_layout = QHBoxLayout()
        special_layout.addWidget(QLabel("Highlight:"))
        self.special_preset_combo = QComboBox()
        self.special_preset_combo.addItem("None")
        from assets.themes import get_preset_names
        try:
            self.special_preset_combo.addItems(get_preset_names())
        except:
            pass
        # Always emit so selecting "None" clears an active highlight
        self.special_preset_combo.currentTextChanged.connect(lambda _: self.style_changed.emit())
        special_layout.addWidget(self.special_preset_combo, 1)
        special_group.setLayout(special_layout)
        general_layout.addWidget(special_group)

        colors_group = QGroupBox("General Colors")
        colors_layout = QVBoxLayout()
        bg_layout = QHBoxLayout()
        bg_layout.addWidget(QLabel("Background:"))
        self.bg_color_button = ColorButton("#FFFFFF")
        self.bg_color_button.color_changed.connect(lambda: self.style_changed.emit())
        bg_layout.addWidget(self.bg_color_button)
        bg_layout.addStretch()
        colors_layout.addLayout(bg_layout)
        gridc_layout = QHBoxLayout()
        gridc_layout.addWidget(QLabel("Grid:"))
        self.grid_color_button = ColorButton("#CCCCCC")
        self.grid_color_button.color_changed.connect(lambda: self.style_changed.emit())
        gridc_layout.addWidget(self.grid_color_button)
        gridc_layout.addStretch()
        colors_layout.addLayout(gridc_layout)
        colors_group.setLayout(colors_layout)
        general_layout.addWidget(colors_group)

        font_group = QGroupBox("Font Settings")
        font_layout = QVBoxLayout()
        family_layout = QHBoxLayout()
        family_layout.addWidget(QLabel("Font Family:"))
        self.font_family_combo = QComboBox()
        self.font_family_combo.addItems([
            'sans-serif', 'serif', 'monospace',
            'Arial', 'Times New Roman', 'Courier New',
            'Calibri', 'Cambria', 'Garamond', 'Georgia',
            'Segoe UI', 'Verdana', 'Tahoma', 'Trebuchet MS',
            'Helvetica', 'Palatino Linotype', 'Book Antiqua',
            'Lucida Sans', 'Lucida Grande', 'Impact',
            'Open Sans', 'Roboto'
        ])
        self.font_family_combo.currentTextChanged.connect(lambda: self.style_changed.emit())
        family_layout.addWidget(self.font_family_combo, 1)
        font_layout.addLayout(family_layout)
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Font Size:"))
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(6, 24)
        self.font_size_spin.setValue(10)
        self.font_size_spin.valueChanged.connect(lambda: self.style_changed.emit())
        size_layout.addWidget(self.font_size_spin)
        size_layout.addStretch()
        font_layout.addLayout(size_layout)
        title_size_layout = QHBoxLayout()
        title_size_layout.addWidget(QLabel("Title Size:"))
        self.title_size_spin = QSpinBox()
        self.title_size_spin.setRange(8, 36)
        self.title_size_spin.setValue(16)
        self.title_size_spin.valueChanged.connect(lambda: self.style_changed.emit())
        title_size_layout.addWidget(self.title_size_spin)
        title_size_layout.addStretch()
        font_layout.addLayout(title_size_layout)
        font_group.setLayout(font_layout)
        general_layout.addWidget(font_group)

        grid_settings_group = QGroupBox("Grid Settings")
        grid_settings_layout = QVBoxLayout()
        self.show_grid_check = QCheckBox("Show Grid")
        self.show_grid_check.setChecked(True)
        self.show_grid_check.stateChanged.connect(lambda: self.style_changed.emit())
        grid_settings_layout.addWidget(self.show_grid_check)
        grid_settings_group.setLayout(grid_settings_layout)
        general_layout.addWidget(grid_settings_group)
        general_layout.addStretch()
        tab.addTab(general_tab, "General")

        # --- Legend tab ---
        legend_tab = QWidget()
        legend_layout = QVBoxLayout(legend_tab)
        legend_layout.setSpacing(8)

        legend_group = QGroupBox("Legend Settings")
        lg_layout = QVBoxLayout()
        self.show_legend_check = QCheckBox("Show Legend")
        self.show_legend_check.setChecked(True)
        self.show_legend_check.stateChanged.connect(lambda: self.style_changed.emit())
        lg_layout.addWidget(self.show_legend_check)
        pos_layout = QHBoxLayout()
        pos_layout.addWidget(QLabel("Position:"))
        self.legend_position_combo = QComboBox()
        self.legend_position_combo.addItems(['best', 'upper right', 'upper left', 'lower right', 'lower left', 'center'])
        self.legend_position_combo.currentTextChanged.connect(lambda: self.style_changed.emit())
        pos_layout.addWidget(self.legend_position_combo, 1)
        lg_layout.addLayout(pos_layout)
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("Legend Title:"))
        self.legend_title_edit = QLineEdit()
        self.legend_title_edit.setPlaceholderText("Optional legend title...")
        self.legend_title_edit.textChanged.connect(lambda: self.style_changed.emit())
        title_layout.addWidget(self.legend_title_edit, 1)
        lg_layout.addLayout(title_layout)
        cols_alpha_layout = QHBoxLayout()
        cols_alpha_layout.addWidget(QLabel("Columns:"))
        self.legend_ncol_spin = QSpinBox()
        self.legend_ncol_spin.setRange(1, 4)
        self.legend_ncol_spin.setValue(1)
        self.legend_ncol_spin.valueChanged.connect(lambda: self.style_changed.emit())
        cols_alpha_layout.addWidget(self.legend_ncol_spin)
        cols_alpha_layout.addWidget(QLabel("Background Transparency:"))
        self.legend_alpha_spin = QDoubleSpinBox()
        self.legend_alpha_spin.setRange(0.0, 1.0)
        self.legend_alpha_spin.setSingleStep(0.05)
        self.legend_alpha_spin.setValue(0.8)
        self.legend_alpha_spin.valueChanged.connect(lambda: self.style_changed.emit())
        cols_alpha_layout.addWidget(self.legend_alpha_spin)
        cols_alpha_layout.addStretch()
        lg_layout.addLayout(cols_alpha_layout)
        spacing_layout = QHBoxLayout()
        spacing_layout.addWidget(QLabel("Label Spacing:"))
        self.legend_labelspacing_spin = QDoubleSpinBox()
        self.legend_labelspacing_spin.setRange(0.0, 5.0)
        self.legend_labelspacing_spin.setSingleStep(0.1)
        self.legend_labelspacing_spin.setValue(0.5)
        self.legend_labelspacing_spin.valueChanged.connect(lambda: self.style_changed.emit())
        spacing_layout.addWidget(self.legend_labelspacing_spin)
        spacing_layout.addWidget(QLabel("Line Length:"))
        self.legend_handlelength_spin = QDoubleSpinBox()
        self.legend_handlelength_spin.setRange(0.5, 10.0)
        self.legend_handlelength_spin.setSingleStep(0.5)
        self.legend_handlelength_spin.setValue(2.0)
        self.legend_handlelength_spin.valueChanged.connect(lambda: self.style_changed.emit())
        spacing_layout.addWidget(self.legend_handlelength_spin)
        spacing_layout.addWidget(QLabel("Text Padding:"))
        self.legend_handletextpad_spin = QDoubleSpinBox()
        self.legend_handletextpad_spin.setRange(0.0, 5.0)
        self.legend_handletextpad_spin.setSingleStep(0.1)
        self.legend_handletextpad_spin.setValue(0.8)
        self.legend_handletextpad_spin.valueChanged.connect(lambda: self.style_changed.emit())
        spacing_layout.addWidget(self.legend_handletextpad_spin)
        spacing_layout.addStretch()
        lg_layout.addLayout(spacing_layout)
        legend_group.setLayout(lg_layout)
        legend_layout.addWidget(legend_group)
        legend_layout.addStretch()
        tab.addTab(legend_tab, "Legend")

        # --- Lines tab ---
        lines_tab = QWidget()
        lines_layout = QVBoxLayout(lines_tab)
        lines_layout.setContentsMargins(0, 0, 0, 0)
        lines_scroll = QScrollArea()
        lines_scroll.setWidgetResizable(True)
        lines_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        lines_widget = QWidget()
        lw_layout = QVBoxLayout(lines_widget)
        self.lines_group = QGroupBox("Line Styles")
        self.lines_layout = QVBoxLayout()
        self.lines_container = QWidget()
        self.lines_container_layout = QVBoxLayout(self.lines_container)
        self.lines_container_layout.setContentsMargins(0, 0, 0, 0)
        self.lines_layout.addWidget(self.lines_container)
        self.lines_group.setLayout(self.lines_layout)
        lw_layout.addWidget(self.lines_group)
        lw_layout.addStretch()
        lines_scroll.setWidget(lines_widget)
        lines_layout.addWidget(lines_scroll)
        tab.addTab(lines_tab, "Lines")
        
    def update_line_styles(self, y_columns: list, theme_colors: list = None, y2_columns: list = None):
        """
        Update line style widgets for selected Y columns.
        
        Args:
            y_columns: List of Y column names
            theme_colors: Optional list of colors from theme
            y2_columns: Optional list of columns that should default to secondary axis
        """
        # Clear existing widgets
        for widget in self.line_widgets.values():
            widget.deleteLater()
        self.line_widgets.clear()

        if y2_columns is None:
            y2_columns = []
        
        # Get theme colors if not provided
        if theme_colors is None:
            from assets.themes import get_theme
            theme = get_theme(self.theme_combo.currentText())
            theme_colors = theme['line_colors']
        
        # Create new widgets
        for i, column in enumerate(y_columns):
            color = theme_colors[i % len(theme_colors)]
            widget = LineStyleWidget(column, color)
            widget.style_changed.connect(lambda: self.style_changed.emit())
            widget.secondary_check.setChecked(column in y2_columns)
            self.line_widgets[column] = widget
            self.lines_container_layout.addWidget(widget)
            
    def apply_theme(self, theme_name: str):
        """Apply a preset theme."""
        from assets.themes import get_theme
        
        try:
            theme = get_theme(theme_name)
            
            # Apply general colors
            self.bg_color_button.update_color(theme['background'])
            self.grid_color_button.update_color(theme['grid'])
            
            # Apply font settings
            if 'font_family' in theme:
                index = self.font_family_combo.findText(theme['font_family'])
                if index >= 0:
                    self.font_family_combo.setCurrentIndex(index)
            
            if 'font_size' in theme:
                self.font_size_spin.setValue(theme['font_size'])
            
            if 'title_fontsize' in theme:
                self.title_size_spin.setValue(theme['title_fontsize'])
            
            # Apply title weight if provided
            if 'title_fontweight' in theme:
                # No direct control for weight in UI; emit change so engine uses theme's weight
                # Title weight is taken from ChartConfig built in main_window
                pass
            
            # Update line colors
            for i, (column, widget) in enumerate(self.line_widgets.items()):
                color = theme['line_colors'][i % len(theme['line_colors'])]
                widget.set_color(color)
            
            self.style_changed.emit()
        except Exception:
            pass  # Ignore theme errors
    
    def get_special_preset_config(self) -> dict:
        """Get period highlights from selected special preset."""
        preset_name = self.special_preset_combo.currentText()
        if preset_name == "None":
            return {'period_highlights': []}
        
        try:
            from assets.themes import get_special_preset
            preset = get_special_preset(preset_name)
            return {'period_highlights': preset.get('period_highlights', [])}
        except Exception:
            return {'period_highlights': []}
            
    def get_config(self) -> dict:
        """Get current style configuration."""
        line_configs = [widget.get_config() for widget in self.line_widgets.values()]
        
        return {
            'background_color': self.bg_color_button.get_color(),
            'grid_color': self.grid_color_button.get_color(),
            'font_family': self.font_family_combo.currentText(),
            'font_size': self.font_size_spin.value(),
            'title_fontsize': self.title_size_spin.value(),
            'show_grid': self.show_grid_check.isChecked(),
            'show_legend': self.show_legend_check.isChecked(),
            'legend_position': self.legend_position_combo.currentText(),
            'legend_title': self.legend_title_edit.text(),
            'legend_ncol': self.legend_ncol_spin.value(),
            'legend_framealpha': self.legend_alpha_spin.value(),
            'legend_labelspacing': self.legend_labelspacing_spin.value(),
            'legend_handlelength': self.legend_handlelength_spin.value(),
            'legend_handletextpad': self.legend_handletextpad_spin.value(),
            'line_configs': line_configs
        }
