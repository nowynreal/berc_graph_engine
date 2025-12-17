"""Excel Chart Generator - Main Application Entry Point.

A professional desktop application for creating highly customizable charts from Excel data.

Features:
- Load Excel files and select data columns
- Fully customizable chart appearance (colors, styles, fonts)
- Dual Y-axis support
- Live preview
- Export to PNG, SVG, and PDF formats

Author: BERC
Version: 1.0.0
"""

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from gui.main_window import MainWindow


def main():
    """Main application entry point."""
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Excel Chart Generator")
    app.setOrganizationName("BERC")
    
    # Set application style
    app.setStyle("Fusion")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
