"""File loading panel for Excel files."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QComboBox, QTableWidget, QTableWidgetItem, QFileDialog,
    QGroupBox, QListWidget, QMessageBox, QLineEdit, QRadioButton,
    QCheckBox, QHeaderView, QAbstractItemView, QButtonGroup
)
from PySide6.QtCore import Signal, Qt
from typing import Optional, List

from utils.excel_reader import ExcelReader


class FilePanel(QWidget):
    """Panel for loading Excel files and selecting data."""
    
    # Signals
    file_loaded = Signal(object)  # Emits ExcelReader
    data_selected = Signal(str, list, list)  # Emits (x_column, y1_columns, y2_columns)
    
    def __init__(self, parent=None):
        """Initialize the file panel."""
        super().__init__(parent)
        
        self.excel_reader = ExcelReader()
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        layout = QVBoxLayout(self)
        
        # File selection group
        file_group = QGroupBox("Excel File")
        file_layout = QVBoxLayout()
        
        # File path display and button
        path_layout = QHBoxLayout()
        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setWordWrap(True)
        self.load_button = QPushButton("Load Excel File...")
        self.load_button.clicked.connect(self.load_file)
        path_layout.addWidget(self.file_path_label, 1)
        path_layout.addWidget(self.load_button)
        file_layout.addLayout(path_layout)
        
        # Sheet selector
        sheet_layout = QHBoxLayout()
        sheet_layout.addWidget(QLabel("Sheet:"))
        self.sheet_combo = QComboBox()
        self.sheet_combo.currentTextChanged.connect(self.load_sheet)
        sheet_layout.addWidget(self.sheet_combo, 1)
        file_layout.addLayout(sheet_layout)
        
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)
        
        # Data preview group
        preview_group = QGroupBox("Data Preview")
        preview_layout = QVBoxLayout()
        
        self.preview_table = QTableWidget()
        self.preview_table.setMaximumHeight(150)
        self.preview_table.setAlternatingRowColors(True)
        preview_layout.addWidget(self.preview_table)
        
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
        
        # Column mapping group
        column_group = QGroupBox("Column Mapping")
        column_layout = QVBoxLayout()

        # Filter/search bar
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        self.filter_edit = QLineEdit()
        self.filter_edit.setPlaceholderText("Type to filter columns...")
        self.filter_edit.textChanged.connect(self.apply_filter)
        filter_layout.addWidget(self.filter_edit, 1)

        # Quick actions
        self.auto_numeric_btn = QPushButton("Auto-select numeric → Y1")
        self.auto_numeric_btn.clicked.connect(self.auto_select_numeric)
        self.clear_y1_btn = QPushButton("Clear Y1")
        self.clear_y1_btn.clicked.connect(lambda: self.clear_column_role('y1'))
        self.clear_y2_btn = QPushButton("Clear Y2")
        self.clear_y2_btn.clicked.connect(lambda: self.clear_column_role('y2'))
        filter_layout.addWidget(self.auto_numeric_btn)
        filter_layout.addWidget(self.clear_y1_btn)
        filter_layout.addWidget(self.clear_y2_btn)
        column_layout.addLayout(filter_layout)

        # Mapping table
        self.map_table = QTableWidget()
        self.map_table.setColumnCount(4)
        self.map_table.setHorizontalHeaderLabels(["Column", "X", "Y1", "Y2"])
        self.map_table.verticalHeader().setVisible(False)
        self.map_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.map_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = self.map_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        column_layout.addWidget(self.map_table)

        # Radio group to enforce single X
        self.x_radio_group = QButtonGroup(self)
        self.x_radio_group.setExclusive(True)

        column_group.setLayout(column_layout)
        layout.addWidget(column_group)

        # Info label
        self.info_label = QLabel("Load an Excel file to begin")
        self.info_label.setStyleSheet("color: gray; font-style: italic;")
        layout.addWidget(self.info_label)
        
        layout.addStretch()
        
    def load_file(self):
        """Open file dialog and load Excel file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Excel File",
            "",
            "Excel Files (*.xlsx *.xls *.xlsm);;All Files (*)"
        )
        
        if not file_path:
            return
        
        try:
            sheet_names = self.excel_reader.load_file(file_path)
            
            # Update UI
            self.file_path_label.setText(file_path)
            self.sheet_combo.clear()
            self.sheet_combo.addItems(sheet_names)
            
            # Load first sheet automatically
            if sheet_names:
                self.load_sheet(sheet_names[0])
            
            self.file_loaded.emit(self.excel_reader)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file:\n{str(e)}")
            
    def load_sheet(self, sheet_name: str):
        """
        Load a specific sheet from the Excel file.
        
        Args:
            sheet_name: Name of the sheet to load
        """
        if not sheet_name:
            return
        
        try:
            df = self.excel_reader.load_sheet(sheet_name)
            
            # Update preview table
            self.update_preview_table(df)
            
            # Update mapping table
            columns = self.excel_reader.get_columns()
            self.populate_mapping_table(columns)
            
            # Update info
            info = self.excel_reader.get_data_info()
            self.info_label.setText(
                f"Loaded: {info['rows']} rows × {info['columns']} columns"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load sheet:\n{str(e)}")
            
    def update_preview_table(self, df):
        """
        Update the preview table with dataframe data.
        
        Args:
            df: Pandas DataFrame to display
        """
        preview = df.head(5)
        
        self.preview_table.setRowCount(len(preview))
        self.preview_table.setColumnCount(len(preview.columns))
        self.preview_table.setHorizontalHeaderLabels(preview.columns.tolist())
        
        for i, row in enumerate(preview.itertuples(index=False)):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.preview_table.setItem(i, j, item)
        
        self.preview_table.resizeColumnsToContents()
        
    def populate_mapping_table(self, columns: List[str]):
        """Populate the mapping table with columns and selection widgets."""
        self.map_table.setRowCount(len(columns))
        self.x_radio_group = QButtonGroup(self)  # reset group
        self.x_radio_group.setExclusive(True)

        numeric_cols = set()
        try:
            numeric_cols = set(self.excel_reader.get_numeric_columns())
        except Exception:
            pass

        default_x = columns[0] if columns else None

        for row, col_name in enumerate(columns):
            # Column label cell
            item = QTableWidgetItem(col_name)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.map_table.setItem(row, 0, item)

            # X radio
            x_radio = QRadioButton()
            x_radio.toggled.connect(lambda checked, r=row: self.on_x_toggled(r, checked))
            self.x_radio_group.addButton(x_radio)
            self.map_table.setCellWidget(row, 1, x_radio)

            # Y1 checkbox
            y1_check = QCheckBox()
            y1_check.stateChanged.connect(lambda _state, r=row: self.on_y_role_changed(r, 'y1'))
            self.map_table.setCellWidget(row, 2, y1_check)

            # Y2 checkbox
            y2_check = QCheckBox()
            y2_check.stateChanged.connect(lambda _state, r=row: self.on_y_role_changed(r, 'y2'))
            self.map_table.setCellWidget(row, 3, y2_check)

            # Defaults: first column as X, numeric others as Y1
            if default_x and col_name == default_x:
                x_radio.setChecked(True)
            elif col_name in numeric_cols:
                y1_check.setChecked(True)

        self.emit_data_selection()

    def on_x_toggled(self, row: int, checked: bool):
        """Ensure X selection is exclusive and not also in Y lists."""
        if not checked:
            return
        # uncheck Y1/Y2 in that row
        y1 = self.map_table.cellWidget(row, 2)
        y2 = self.map_table.cellWidget(row, 3)
        if isinstance(y1, QCheckBox):
            y1.blockSignals(True); y1.setChecked(False); y1.blockSignals(False)
        if isinstance(y2, QCheckBox):
            y2.blockSignals(True); y2.setChecked(False); y2.blockSignals(False)
        self.emit_data_selection()

    def on_y_role_changed(self, row: int, role: str):
        """Keep Y1/Y2 mutually exclusive per column and not equal to X."""
        # If a Y role is checked, uncheck the other
        y1 = self.map_table.cellWidget(row, 2)
        y2 = self.map_table.cellWidget(row, 3)
        x_radio = self.map_table.cellWidget(row, 1)
        if role == 'y1' and isinstance(y1, QCheckBox) and y1.isChecked():
            if isinstance(y2, QCheckBox):
                y2.blockSignals(True); y2.setChecked(False); y2.blockSignals(False)
            if isinstance(x_radio, QRadioButton) and x_radio.isChecked():
                x_radio.setChecked(False)
        elif role == 'y2' and isinstance(y2, QCheckBox) and y2.isChecked():
            if isinstance(y1, QCheckBox):
                y1.blockSignals(True); y1.setChecked(False); y1.blockSignals(False)
            if isinstance(x_radio, QRadioButton) and x_radio.isChecked():
                x_radio.setChecked(False)
        self.emit_data_selection()

    def apply_filter(self, text: str):
        """Filter rows in mapping table by column name substring."""
        t = (text or '').lower()
        for row in range(self.map_table.rowCount()):
            name = self.map_table.item(row, 0).text().lower() if self.map_table.item(row,0) else ''
            self.map_table.setRowHidden(row, t not in name)

    def clear_column_role(self, role: str):
        for row in range(self.map_table.rowCount()):
            widget = self.map_table.cellWidget(row, 2 if role=='y1' else 3)
            if isinstance(widget, QCheckBox):
                widget.setChecked(False)
        self.emit_data_selection()

    def auto_select_numeric(self):
        numeric = set()
        try:
            numeric = set(self.excel_reader.get_numeric_columns())
        except Exception:
            pass
        # Clear Y1 first
        self.clear_column_role('y1')
        # Set Y1 for numeric columns except X
        for row in range(self.map_table.rowCount()):
            name = self.map_table.item(row, 0).text()
            x_radio = self.map_table.cellWidget(row, 1)
            if name in numeric and not (isinstance(x_radio, QRadioButton) and x_radio.isChecked()):
                y1 = self.map_table.cellWidget(row, 2)
                if isinstance(y1, QCheckBox):
                    y1.setChecked(True)
                    
    def emit_data_selection(self):
        """Emit signal with current data selection."""
        x_column = None
        y1_columns = []
        y2_columns = []
        for row in range(self.map_table.rowCount()):
            item = self.map_table.item(row, 0)
            if item is None:  # Skip if cell not yet populated
                continue
            name = item.text()
            xr = self.map_table.cellWidget(row, 1)
            y1 = self.map_table.cellWidget(row, 2)
            y2 = self.map_table.cellWidget(row, 3)
            if isinstance(xr, QRadioButton) and xr.isChecked():
                x_column = name
            if isinstance(y1, QCheckBox) and y1.isChecked():
                y1_columns.append(name)
            if isinstance(y2, QCheckBox) and y2.isChecked():
                y2_columns.append(name)

        if x_column and (y1_columns or y2_columns):
            self.data_selected.emit(x_column, y1_columns, y2_columns)
            
    def get_selected_data(self):
        """
        Get the currently selected data columns.
        
        Returns:
            Tuple of (x_column, y1_columns, y2_columns) or (None, None, None)
        """
        x_column = None
        y1_columns = []
        y2_columns = []
        for row in range(self.map_table.rowCount()):
            name = self.map_table.item(row, 0).text()
            xr = self.map_table.cellWidget(row, 1)
            y1 = self.map_table.cellWidget(row, 2)
            y2 = self.map_table.cellWidget(row, 3)
            if isinstance(xr, QRadioButton) and xr.isChecked():
                x_column = name
            if isinstance(y1, QCheckBox) and y1.isChecked():
                y1_columns.append(name)
            if isinstance(y2, QCheckBox) and y2.isChecked():
                y2_columns.append(name)

        if x_column and (y1_columns or y2_columns):
            return x_column, y1_columns, y2_columns
        return None, None, None
    
    def get_plot_data(self):
        """
        Get data prepared for plotting.
        
        Returns:
            Dictionary with plot data or None
        """
        x_column, y1_columns, y2_columns = self.get_selected_data()
        combined = (y1_columns or []) + (y2_columns or [])
        all_y = list(dict.fromkeys(combined))  # preserve order while removing duplicates
        
        if x_column and all_y:
            try:
                return self.excel_reader.get_plot_data(x_column, all_y)
            except Exception as e:
                QMessageBox.warning(self, "Warning", f"Failed to get plot data:\n{str(e)}")
                return None
        return None
