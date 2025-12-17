"""Excel file reading and data extraction utilities."""

import pandas as pd
from pathlib import Path
from typing import List, Dict, Optional, Any


class ExcelReader:
    """Handles Excel file loading and data extraction."""
    
    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize the Excel reader.
        
        Args:
            file_path: Path to the Excel file to load
        """
        self.file_path = file_path
        self.excel_file: Optional[pd.ExcelFile] = None
        self.current_sheet: Optional[str] = None
        self.dataframe: Optional[pd.DataFrame] = None
        
    def load_file(self, file_path: str) -> List[str]:
        """
        Load an Excel file and return available sheet names.
        
        Args:
            file_path: Path to the Excel file
            
        Returns:
            List of sheet names in the workbook
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is not a valid Excel file
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if path.suffix.lower() not in ['.xlsx', '.xls', '.xlsm']:
            raise ValueError(f"Invalid file format: {path.suffix}. Expected .xlsx, .xls, or .xlsm")
        
        try:
            self.file_path = file_path
            self.excel_file = pd.ExcelFile(file_path)
            return self.excel_file.sheet_names
        except Exception as e:
            raise ValueError(f"Failed to load Excel file: {str(e)}")
    
    def load_sheet(self, sheet_name: str) -> pd.DataFrame:
        """
        Load a specific sheet from the Excel file.
        
        Args:
            sheet_name: Name of the sheet to load
            
        Returns:
            DataFrame containing the sheet data
            
        Raises:
            ValueError: If no file is loaded or sheet doesn't exist
        """
        if self.excel_file is None:
            raise ValueError("No Excel file loaded. Call load_file() first.")
        
        if sheet_name not in self.excel_file.sheet_names:
            raise ValueError(f"Sheet '{sheet_name}' not found in workbook")
        
        try:
            self.current_sheet = sheet_name
            self.dataframe = pd.read_excel(self.excel_file, sheet_name=sheet_name)
            
            # Clean column names - remove leading/trailing whitespace
            self.dataframe.columns = self.dataframe.columns.str.strip()
            
            return self.dataframe
        except Exception as e:
            raise ValueError(f"Failed to load sheet '{sheet_name}': {str(e)}")
    
    def get_columns(self) -> List[str]:
        """
        Get list of column names from the current sheet.
        
        Returns:
            List of column names
            
        Raises:
            ValueError: If no sheet is loaded
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        return self.dataframe.columns.tolist()
    
    def get_numeric_columns(self) -> List[str]:
        """
        Get list of numeric column names from the current sheet.
        
        Returns:
            List of numeric column names
            
        Raises:
            ValueError: If no sheet is loaded
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        numeric_columns = self.dataframe.select_dtypes(include=['number']).columns.tolist()
        return numeric_columns
    
    def get_column_data(self, column_name: str) -> pd.Series:
        """
        Get data from a specific column.
        
        Args:
            column_name: Name of the column
            
        Returns:
            Series containing the column data
            
        Raises:
            ValueError: If no sheet is loaded or column doesn't exist
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        if column_name not in self.dataframe.columns:
            raise ValueError(f"Column '{column_name}' not found in sheet")
        
        return self.dataframe[column_name]
    
    def get_data_preview(self, rows: int = 5) -> pd.DataFrame:
        """
        Get a preview of the loaded data.
        
        Args:
            rows: Number of rows to preview
            
        Returns:
            DataFrame with the first N rows
            
        Raises:
            ValueError: If no sheet is loaded
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        return self.dataframe.head(rows)
    
    def get_data_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded data.
        
        Returns:
            Dictionary containing data info (rows, columns, types)
            
        Raises:
            ValueError: If no sheet is loaded
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        return {
            'rows': len(self.dataframe),
            'columns': len(self.dataframe.columns),
            'column_names': self.dataframe.columns.tolist(),
            'column_types': self.dataframe.dtypes.to_dict(),
            'memory_usage': self.dataframe.memory_usage(deep=True).sum(),
            'missing_values': self.dataframe.isnull().sum().to_dict()
        }
    
    def get_plot_data(self, x_column: str, y_columns: List[str]) -> Dict[str, pd.Series]:
        """
        Get data prepared for plotting.
        
        Args:
            x_column: Name of the X-axis column
            y_columns: List of Y-axis column names
            
        Returns:
            Dictionary with 'x' and 'y' data
            
        Raises:
            ValueError: If columns don't exist or data is invalid
        """
        if self.dataframe is None:
            raise ValueError("No sheet loaded. Call load_sheet() first.")
        
        # Validate columns exist
        all_columns = [x_column] + y_columns
        missing = [col for col in all_columns if col not in self.dataframe.columns]
        if missing:
            raise ValueError(f"Columns not found: {', '.join(missing)}")
        
        # Extract data
        data = {'x': self.dataframe[x_column].copy()}
        
        for y_col in y_columns:
            data[y_col] = self.dataframe[y_col].copy()
        
        # Remove rows with NaN values in selected columns
        mask = pd.notna(data['x'])
        for y_col in y_columns:
            mask &= pd.notna(data[y_col])
        
        return {key: series[mask].reset_index(drop=True) for key, series in data.items()}
    
    def close(self):
        """Close the Excel file and clean up resources."""
        if self.excel_file is not None:
            self.excel_file.close()
            self.excel_file = None
        self.dataframe = None
        self.current_sheet = None
