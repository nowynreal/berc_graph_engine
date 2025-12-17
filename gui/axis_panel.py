"""Axis configuration panel for chart axes."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QSpinBox, QDoubleSpinBox, QGroupBox, QCheckBox, QComboBox, QTabWidget, QScrollArea
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QDoubleValidator


class AxisControlWidget(QWidget):
    """Widget for configuring a single axis."""
    
    settings_changed = Signal()
    
    def __init__(self, axis_name: str, parent=None):
        """
        Initialize the axis control widget.
        
        Args:
            axis_name: Name of the axis (e.g., "X-Axis", "Y-Axis")
        """
        super().__init__(parent)
        
        self.axis_name = axis_name
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        
        # Label
        label_layout = QHBoxLayout()
        label_layout.addWidget(QLabel("Label:"))
        self.label_edit = QLineEdit()
        self.label_edit.setPlaceholderText(f"{self.axis_name} Label")
        self.label_edit.textChanged.connect(lambda: self.settings_changed.emit())
        label_layout.addWidget(self.label_edit, 1)
        layout.addLayout(label_layout)
        
        # Min/Max values
        minmax_layout = QHBoxLayout()
        
        # Min
        minmax_layout.addWidget(QLabel("Min:"))
        self.min_edit = QLineEdit()
        self.min_edit.setPlaceholderText("Auto")
        self.min_edit.setMaximumWidth(80)
        validator = QDoubleValidator()
        self.min_edit.setValidator(validator)
        self.min_edit.textChanged.connect(lambda: self.settings_changed.emit())
        minmax_layout.addWidget(self.min_edit)
        
        # Max
        minmax_layout.addWidget(QLabel("Max:"))
        self.max_edit = QLineEdit()
        self.max_edit.setPlaceholderText("Auto")
        self.max_edit.setMaximumWidth(80)
        self.max_edit.setValidator(validator)
        self.max_edit.textChanged.connect(lambda: self.settings_changed.emit())
        minmax_layout.addWidget(self.max_edit)
        
        minmax_layout.addStretch()
        layout.addLayout(minmax_layout)
        
        # Tick rotation
        rotation_layout = QHBoxLayout()
        rotation_layout.addWidget(QLabel("Tick Rotation:"))
        self.rotation_spin = QSpinBox()
        self.rotation_spin.setRange(-90, 90)
        self.rotation_spin.setValue(0)
        self.rotation_spin.setSuffix("°")
        self.rotation_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        rotation_layout.addWidget(self.rotation_spin)
        rotation_layout.addStretch()
        layout.addLayout(rotation_layout)

        # Tick step
        step_layout = QHBoxLayout()
        step_layout.addWidget(QLabel("Tick Step:"))
        self.step_spin = QDoubleSpinBox()
        self.step_spin.setRange(0.0, 1e9)
        self.step_spin.setDecimals(4)
        self.step_spin.setValue(0.0)
        self.step_spin.setSingleStep(1.0)
        self.step_spin.setSpecialValueText("Auto")
        self.step_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        step_layout.addWidget(self.step_spin)
        step_layout.addStretch()
        layout.addLayout(step_layout)

        # Categorical toggle (for X axis primarily)
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel("Categorical (show all labels):"))
        self.categorical_check = QCheckBox()
        self.categorical_check.stateChanged.connect(lambda: self.settings_changed.emit())
        cat_layout.addWidget(self.categorical_check)
        cat_layout.addStretch()
        layout.addLayout(cat_layout)

        # Hide labels but keep grid/ticks
        hide_layout = QHBoxLayout()
        hide_layout.addWidget(QLabel("Hide labels (grid only):"))
        self.hide_labels_check = QCheckBox()
        self.hide_labels_check.stateChanged.connect(lambda: self.settings_changed.emit())
        hide_layout.addWidget(self.hide_labels_check)
        hide_layout.addStretch()
        layout.addLayout(hide_layout)

        # Grouped categorical (year/quarter pattern)
        grouped_layout = QHBoxLayout()
        grouped_layout.addWidget(QLabel("Group labels (year only):"))
        self.grouped_categorical_check = QCheckBox()
        self.grouped_categorical_check.setToolTip("Show only group prefix (e.g., '2006 q1' → '2006')")
        self.grouped_categorical_check.stateChanged.connect(lambda: self.settings_changed.emit())
        grouped_layout.addWidget(self.grouped_categorical_check)
        grouped_layout.addStretch()
        layout.addLayout(grouped_layout)

        # Scale
        scale_layout = QHBoxLayout()
        scale_layout.addWidget(QLabel("Scale:"))
        self.scale_combo = QComboBox()
        self.scale_combo.addItems(["Linear", "Log"])
        self.scale_combo.currentTextChanged.connect(lambda: self.settings_changed.emit())
        scale_layout.addWidget(self.scale_combo)
        scale_layout.addStretch()
        layout.addLayout(scale_layout)

        # Value format
        fmt_layout = QHBoxLayout()
        fmt_layout.addWidget(QLabel("Value Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems([
            "Auto",
            "Decimal",
            "Scientific",
            "Percent",
            "Integer"
        ])
        self.format_combo.currentTextChanged.connect(lambda: self.settings_changed.emit())
        fmt_layout.addWidget(self.format_combo)
        fmt_layout.addStretch()
        layout.addLayout(fmt_layout)
        
        layout.addStretch()
    
    def get_config(self) -> dict:
        """Get axis configuration."""
        return {
            'label': self.label_edit.text(),
            'min_value': self.min_edit.text() if self.min_edit.text() else None,
            'max_value': self.max_edit.text() if self.max_edit.text() else None,
            'tick_rotation': self.rotation_spin.value(),
            'tick_step': self.step_spin.value() if self.step_spin.value() > 0 else 0,
            'categorical': self.categorical_check.isChecked(),
            'hide_labels': self.hide_labels_check.isChecked(),
            'grouped_categorical': self.grouped_categorical_check.isChecked(),
            'scale': self.scale_combo.currentText().lower(),
            'value_format': self.format_combo.currentText().lower(),
        }
    
    def set_label(self, label: str):
        """Set the label."""
        self.label_edit.setText(label)


class AxisPanel(QWidget):
    """Panel for configuring chart axes and figure properties."""
    
    settings_changed = Signal()
    
    def __init__(self, parent=None):
        """Initialize the axis panel."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface with tabbed layout."""
        layout = QVBoxLayout(self)
        
        # Create tab widget
        tabs = QTabWidget()
        
        # ==================== Titles Tab ====================
        titles_tab = QWidget()
        titles_layout = QVBoxLayout(titles_tab)
        
        # Main title
        main_title_layout = QHBoxLayout()
        main_title_layout.addWidget(QLabel("Title:"))
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Enter chart title...")
        self.title_edit.setText("Chart")
        self.title_edit.textChanged.connect(lambda: self.settings_changed.emit())
        main_title_layout.addWidget(self.title_edit, 1)
        titles_layout.addLayout(main_title_layout)

        # Title alignment and offset
        align_layout = QHBoxLayout()
        align_layout.addWidget(QLabel("Title Align:"))
        self.title_align_combo = QComboBox()
        self.title_align_combo.addItems(["Left", "Center", "Right"]) 
        self.title_align_combo.currentTextChanged.connect(lambda: self.settings_changed.emit())
        align_layout.addWidget(self.title_align_combo)
        
        align_layout.addWidget(QLabel("Vertical Offset:"))
        self.title_yoffset_spin = QDoubleSpinBox()
        self.title_yoffset_spin.setRange(0.8, 1.2)
        self.title_yoffset_spin.setSingleStep(0.01)
        self.title_yoffset_spin.setValue(1.0)
        self.title_yoffset_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        align_layout.addWidget(self.title_yoffset_spin)
        align_layout.addStretch()
        titles_layout.addLayout(align_layout)

        # Subtitle
        sub_layout = QHBoxLayout()
        sub_layout.addWidget(QLabel("Subtitle:"))
        self.subtitle_edit = QLineEdit()
        self.subtitle_edit.setPlaceholderText("Optional subtitle...")
        self.subtitle_edit.textChanged.connect(lambda: self.settings_changed.emit())
        sub_layout.addWidget(self.subtitle_edit, 1)
        
        sub_layout.addWidget(QLabel("Size:"))
        self.subtitle_size_spin = QSpinBox()
        self.subtitle_size_spin.setRange(6, 24)
        self.subtitle_size_spin.setValue(12)
        self.subtitle_size_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        sub_layout.addWidget(self.subtitle_size_spin)
        
        self.subtitle_bold_check = QCheckBox("Bold")
        self.subtitle_bold_check.stateChanged.connect(lambda: self.settings_changed.emit())
        sub_layout.addWidget(self.subtitle_bold_check)
        sub_layout.addStretch()
        titles_layout.addLayout(sub_layout)

        # Subtitle alignment and offset
        sub_align_layout = QHBoxLayout()
        sub_align_layout.addWidget(QLabel("Subtitle Align:"))
        self.subtitle_align_combo = QComboBox()
        self.subtitle_align_combo.addItems(["Chart Left", "Chart Center", "Chart Right", "Figure Left", "Figure Right"])
        self.subtitle_align_combo.setCurrentText("Chart Center")
        self.subtitle_align_combo.currentTextChanged.connect(lambda: self.settings_changed.emit())
        sub_align_layout.addWidget(self.subtitle_align_combo)

        sub_align_layout.addWidget(QLabel("Offset from Title:"))
        self.subtitle_yoffset_spin = QDoubleSpinBox()
        self.subtitle_yoffset_spin.setRange(-0.3, 0.1)
        self.subtitle_yoffset_spin.setSingleStep(0.01)
        self.subtitle_yoffset_spin.setValue(-0.06)
        self.subtitle_yoffset_spin.setToolTip("Vertical distance from title (negative = below)")
        self.subtitle_yoffset_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        sub_align_layout.addWidget(self.subtitle_yoffset_spin)
        sub_align_layout.addStretch()
        titles_layout.addLayout(sub_align_layout)
        
        titles_layout.addStretch()
        tabs.addTab(titles_tab, "Titles")
        
        # ==================== X-Axis Tab ====================
        x_tab = QWidget()
        x_layout = QVBoxLayout(x_tab)
        
        self.x_axis_widget = AxisControlWidget("X-Axis")
        self.x_axis_widget.settings_changed.connect(lambda: self.settings_changed.emit())
        x_layout.addWidget(self.x_axis_widget)

        # Bold label toggle
        x_bold_layout = QHBoxLayout()
        self.x_label_bold_check = QCheckBox("Bold label")
        self.x_label_bold_check.stateChanged.connect(lambda: self.settings_changed.emit())
        x_bold_layout.addWidget(self.x_label_bold_check)
        x_bold_layout.addStretch()
        x_layout.addLayout(x_bold_layout)
        
        x_layout.addStretch()
        tabs.addTab(x_tab, "X-Axis")
        
        # ==================== Y1-Axis Tab ====================
        y_tab = QWidget()
        y_layout = QVBoxLayout(y_tab)
        
        self.y_axis_widget = AxisControlWidget("Y-Axis")
        self.y_axis_widget.settings_changed.connect(lambda: self.settings_changed.emit())
        y_layout.addWidget(self.y_axis_widget)

        y_bold_layout = QHBoxLayout()
        self.y_label_bold_check = QCheckBox("Bold label")
        self.y_label_bold_check.stateChanged.connect(lambda: self.settings_changed.emit())
        y_bold_layout.addWidget(self.y_label_bold_check)
        y_bold_layout.addStretch()
        y_layout.addLayout(y_bold_layout)
        
        y_layout.addStretch()
        tabs.addTab(y_tab, "Y1-Axis")
        
        # ==================== Y2-Axis Tab ====================
        y2_tab = QWidget()
        y2_layout = QVBoxLayout(y2_tab)
        
        # Enable checkbox
        self.enable_y2_check = QCheckBox("Enable Secondary Y-Axis")
        self.enable_y2_check.stateChanged.connect(self.toggle_y2_axis)
        self.enable_y2_check.stateChanged.connect(lambda: self.settings_changed.emit())
        y2_layout.addWidget(self.enable_y2_check)
        
        self.y2_axis_widget = AxisControlWidget("Y2-Axis")
        self.y2_axis_widget.settings_changed.connect(lambda: self.settings_changed.emit())
        y2_layout.addWidget(self.y2_axis_widget)

        y2_bold_layout = QHBoxLayout()
        self.y2_label_bold_check = QCheckBox("Bold label")
        self.y2_label_bold_check.stateChanged.connect(lambda: self.settings_changed.emit())
        y2_bold_layout.addWidget(self.y2_label_bold_check)
        y2_bold_layout.addStretch()
        y2_layout.addLayout(y2_bold_layout)
        
        y2_layout.addStretch()
        tabs.addTab(y2_tab, "Y2-Axis")
        
        # ==================== Figure Tab ====================
        fig_tab = QWidget()
        fig_layout = QVBoxLayout(fig_tab)
        
        size_layout = QHBoxLayout()
        
        size_layout.addWidget(QLabel("Width:"))
        self.width_spin = QDoubleSpinBox()
        self.width_spin.setRange(4.0, 20.0)
        self.width_spin.setValue(10.0)
        self.width_spin.setSingleStep(0.5)
        self.width_spin.setSuffix(" in")
        self.width_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        size_layout.addWidget(self.width_spin)
        
        size_layout.addWidget(QLabel("Height:"))
        self.height_spin = QDoubleSpinBox()
        self.height_spin.setRange(3.0, 15.0)
        self.height_spin.setValue(6.0)
        self.height_spin.setSingleStep(0.5)
        self.height_spin.setSuffix(" in")
        self.height_spin.valueChanged.connect(lambda: self.settings_changed.emit())
        size_layout.addWidget(self.height_spin)
        
        size_layout.addStretch()
        fig_layout.addLayout(size_layout)
        fig_layout.addStretch()
        tabs.addTab(fig_tab, "Figure")
        
        layout.addWidget(tabs)
        layout.addStretch()
        
    def toggle_y2_axis(self, state):
        """Enable/disable secondary Y-axis controls."""
        # Keep inputs editable so labels can be adjusted anytime; checkbox only controls inclusion
        self.y2_axis_widget.setEnabled(True)
        
    def get_config(self) -> dict:
        """Get axis configuration."""
        cfg = {
            'title': self.title_edit.text(),
            'title_loc': self.title_align_combo.currentText().lower(),
            'title_yoffset': self.title_yoffset_spin.value(),
            'subtitle': self.subtitle_edit.text(),
            'subtitle_fontsize': self.subtitle_size_spin.value(),
            'subtitle_fontweight': 'bold' if self.subtitle_bold_check.isChecked() else 'normal',
            'subtitle_loc': self.subtitle_align_combo.currentText().lower().replace(' ', '_'),
            'subtitle_yoffset': self.subtitle_yoffset_spin.value(),
            'x_axis': self.x_axis_widget.get_config(),
            'y_axis': self.y_axis_widget.get_config(),
            'y2_axis': self.y2_axis_widget.get_config() if self.enable_y2_check.isChecked() else None,
            'figure_width': self.width_spin.value(),
            'figure_height': self.height_spin.value()
        }

        # Apply bold toggles to axis label fontweight
        cfg['x_axis']['label_fontweight'] = 'bold' if self.x_label_bold_check.isChecked() else 'normal'
        cfg['y_axis']['label_fontweight'] = 'bold' if self.y_label_bold_check.isChecked() else 'normal'
        if cfg['y2_axis']:
            cfg['y2_axis']['label_fontweight'] = 'bold' if self.y2_label_bold_check.isChecked() else 'normal'

        return cfg
        
    def set_x_label_suggestion(self, label: str):
        """Set a suggested X-axis label."""
        if not self.x_axis_widget.label_edit.text():
            self.x_axis_widget.set_label(label)
            
    def set_y_label_suggestion(self, label: str):
        """Set a suggested Y-axis label."""
        if not self.y_axis_widget.label_edit.text():
            self.y_axis_widget.set_label(label)

    def set_y2_label_suggestion(self, label: str):
        """Set a suggested Y2-axis label and enable Y2."""
        if not self.y2_axis_widget.label_edit.text():
            self.y2_axis_widget.set_label(label)
        # Auto-enable Y2 axis when a suggestion is provided
        if not self.enable_y2_check.isChecked():
            self.enable_y2_check.setChecked(True)
