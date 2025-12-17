"""Export configuration panel for saving charts."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QComboBox, QSpinBox, QGroupBox, QFileDialog, QMessageBox,
    QLineEdit
)
from PySide6.QtCore import Signal
from pathlib import Path


class ExportPanel(QWidget):
    """Panel for configuring chart export settings."""
    
    export_requested = Signal(str, str, int)  # (output_path, format, dpi)
    
    def __init__(self, parent=None):
        """Initialize the export panel."""
        super().__init__(parent)
        
        self.last_directory = str(Path.home())
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        layout = QVBoxLayout(self)
        
        # Format selection
        format_group = QGroupBox("Output Format")
        format_layout = QVBoxLayout()
        
        format_select_layout = QHBoxLayout()
        format_select_layout.addWidget(QLabel("Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['PNG (Raster)', 'SVG (Vector)', 'PDF (Vector)'])
        self.format_combo.setItemData(0, 'png')
        self.format_combo.setItemData(1, 'svg')
        self.format_combo.setItemData(2, 'pdf')
        self.format_combo.currentIndexChanged.connect(self.update_format_settings)
        format_select_layout.addWidget(self.format_combo, 1)
        format_layout.addLayout(format_select_layout)
        
        format_group.setLayout(format_layout)
        layout.addWidget(format_group)
        
        # DPI settings (for PNG)
        self.dpi_group = QGroupBox("Resolution (DPI)")
        dpi_layout = QVBoxLayout()
        
        dpi_select_layout = QHBoxLayout()
        dpi_select_layout.addWidget(QLabel("DPI:"))
        self.dpi_spin = QSpinBox()
        self.dpi_spin.setRange(72, 600)
        self.dpi_spin.setValue(300)
        self.dpi_spin.setSingleStep(50)
        dpi_select_layout.addWidget(self.dpi_spin)
        
        # DPI presets
        preset_layout = QHBoxLayout()
        preset_layout.addWidget(QLabel("Presets:"))
        
        dpi_72_btn = QPushButton("72 (Screen)")
        dpi_72_btn.clicked.connect(lambda: self.dpi_spin.setValue(72))
        preset_layout.addWidget(dpi_72_btn)
        
        dpi_150_btn = QPushButton("150 (Draft)")
        dpi_150_btn.clicked.connect(lambda: self.dpi_spin.setValue(150))
        preset_layout.addWidget(dpi_150_btn)
        
        dpi_300_btn = QPushButton("300 (Print)")
        dpi_300_btn.clicked.connect(lambda: self.dpi_spin.setValue(300))
        preset_layout.addWidget(dpi_300_btn)
        
        dpi_600_btn = QPushButton("600 (High)")
        dpi_600_btn.clicked.connect(lambda: self.dpi_spin.setValue(600))
        preset_layout.addWidget(dpi_600_btn)
        
        dpi_layout.addLayout(dpi_select_layout)
        dpi_layout.addLayout(preset_layout)
        
        self.dpi_group.setLayout(dpi_layout)
        layout.addWidget(self.dpi_group)
        
        # Output location
        location_group = QGroupBox("Output Location")
        location_layout = QVBoxLayout()
        
        path_layout = QHBoxLayout()
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("Select output location...")
        self.path_edit.setReadOnly(True)
        path_layout.addWidget(self.path_edit, 1)
        
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_output_location)
        path_layout.addWidget(browse_btn)
        
        location_layout.addLayout(path_layout)
        
        location_group.setLayout(location_layout)
        layout.addWidget(location_group)
        
        # Export button
        export_layout = QHBoxLayout()
        self.export_button = QPushButton("Export Chart")
        self.export_button.clicked.connect(self.request_export)
        self.export_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D4;
                color: white;
                padding: 8px 16px;
                font-weight: bold;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #106EBE;
            }
            QPushButton:pressed {
                background-color: #005A9E;
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
            }
        """)
        export_layout.addStretch()
        export_layout.addWidget(self.export_button)
        export_layout.addStretch()
        layout.addLayout(export_layout)
        
        # Info label
        self.info_label = QLabel("Configure export settings and click Export")
        self.info_label.setStyleSheet("color: gray; font-style: italic;")
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)
        
        layout.addStretch()
        
    def update_format_settings(self):
        """Update UI based on selected format."""
        format_type = self.format_combo.currentData()
        
        # DPI only applies to PNG
        self.dpi_group.setEnabled(format_type == 'png')
        
    def browse_output_location(self):
        """Open file dialog to select output location."""
        format_type = self.format_combo.currentData()
        
        # Set file filter based on format
        if format_type == 'png':
            file_filter = "PNG Image (*.png)"
            default_ext = ".png"
        elif format_type == 'svg':
            file_filter = "SVG Vector (*.svg)"
            default_ext = ".svg"
        else:  # pdf
            file_filter = "PDF Document (*.pdf)"
            default_ext = ".pdf"
        
        # Suggest filename
        default_name = f"chart{default_ext}"
        default_path = str(Path(self.last_directory) / default_name)
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Chart As",
            default_path,
            file_filter
        )
        
        if file_path:
            # Ensure correct extension
            path = Path(file_path)
            if path.suffix.lower() != default_ext:
                file_path = str(path.with_suffix(default_ext))
            
            self.path_edit.setText(file_path)
            self.last_directory = str(Path(file_path).parent)
            
    def request_export(self):
        """Request chart export with current settings."""
        output_path = self.path_edit.text()
        
        if not output_path:
            QMessageBox.warning(
                self,
                "No Output Path",
                "Please select an output location first."
            )
            return
        
        format_type = self.format_combo.currentData()
        dpi = self.dpi_spin.value() if format_type == 'png' else 100
        
        self.export_requested.emit(output_path, format_type, dpi)
        
    def set_export_success(self, file_path: str):
        """Display export success message."""
        self.info_label.setText(f"✓ Successfully exported to:\n{file_path}")
        self.info_label.setStyleSheet("color: green; font-style: italic;")
        
    def set_export_error(self, error_message: str):
        """Display export error message."""
        self.info_label.setText(f"✗ Export failed:\n{error_message}")
        self.info_label.setStyleSheet("color: red; font-style: italic;")
        
    def reset_info(self):
        """Reset info label to default."""
        self.info_label.setText("Configure export settings and click Export")
        self.info_label.setStyleSheet("color: gray; font-style: italic;")
