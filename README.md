# Excel Chart Generator

A professional desktop GUI application for creating highly customizable charts from Excel data files. Built with PySide6 (Qt) and matplotlib, this tool provides researchers and analysts with a powerful, user-friendly interface for data visualization.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎯 Features

### Data Loading
- **Excel File Support**: Load `.xlsx`, `.xls`, and `.xlsm` files
- **Sheet Selection**: Choose from multiple worksheets
- **Column Preview**: View data before plotting
- **Flexible Selection**: Pick X-axis and multiple Y-axis columns
- **Dual Y-Axis**: Support for secondary Y-axis with independent scaling

### Chart Customization

#### Style Controls
- **6 Preset Themes**: Light, Dark, Scientific, Vibrant, Pastel, Monochrome
- **Custom Colors**: Individual color pickers for background, grid, and each data series
- **Line Styles**: Solid, dashed, dotted, dash-dot
- **Line Width**: Adjustable from 0.5 to 10.0 pixels
- **Markers**: Circle, square, triangle, diamond, plus, cross, or none
- **Fonts**: Multiple font families and adjustable sizes
- **Grid Control**: Toggle grid visibility with custom colors

#### Axis Configuration
- **Axis Labels**: Custom labels for X, Y1, and Y2 axes
- **Value Ranges**: Set minimum and maximum values (or auto-scale)
- **Tick Rotation**: Rotate tick labels from -90° to +90°
- **Figure Size**: Adjustable width (4-20 inches) and height (3-15 inches)

#### Legend
- **Toggle Visibility**: Show or hide legend
- **Position Control**: Best, upper/lower right/left, center
- **Multi-column Support**: Organize legend entries

### Live Preview
- **Real-time Updates**: See changes instantly as you adjust settings
- **Debounced Rendering**: Smooth performance during rapid changes
- **Embedded Preview**: No need to export to see results

### Export Options
- **PNG Export**: High-quality raster images with adjustable DPI (72-600)
  - Screen quality: 72 DPI
  - Draft quality: 150 DPI
  - Print quality: 300 DPI
  - High quality: 600 DPI
- **SVG Export**: Scalable vector graphics for publications
- **PDF Export**: Professional documents ready for printing
- **File Browser**: Easy output location selection

## 📋 Requirements

- Python 3.8 or higher
- Windows, macOS, or Linux

## 🚀 Installation

### Step 1: Clone or Download

Download this project to your local machine or clone it:

```bash
git clone <repository-url>
cd berc_grapher
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **PySide6** (≥6.6.0): Qt framework for GUI
- **pandas** (≥2.0.0): Data manipulation and Excel reading
- **matplotlib** (≥3.7.0): Chart rendering engine
- **openpyxl** (≥3.1.0): Excel file format support

## 🎮 Usage

### Running the Application

```bash
python main.py
```

### Step-by-Step Guide

#### 1. Load Data
1. Click the **"Data"** tab
2. Click **"Load Excel File..."**
3. Select your Excel file
4. Choose the sheet from the dropdown
5. Preview your data in the table

#### 2. Select Columns
1. Choose your **X-Axis column** from the dropdown
2. Select one or more **Y-Axis columns** from the list (Ctrl+Click for multiple)
3. Data will automatically be validated

#### 3. Customize Style
1. Click the **"Style"** tab
2. Choose a preset theme or customize:
   - Background and grid colors
   - Font family and sizes
   - Individual line colors, styles, widths, and markers
   - Enable/disable grid and legend
3. Mark lines for secondary Y-axis with the **Y2** checkbox

#### 4. Configure Axes
1. Click the **"Axes"** tab
2. Set chart title
3. Configure X, Y1, and optionally Y2 axes:
   - Custom labels
   - Min/Max values (leave blank for auto)
   - Tick rotation
4. Adjust figure dimensions

#### 5. Preview
- Chart updates automatically in the preview panel
- All changes reflect immediately

#### 6. Export
1. Click the **"Export"** tab
2. Choose output format (PNG, SVG, or PDF)
3. Set DPI for PNG (if applicable)
4. Click **"Browse..."** to select save location
5. Click **"Export Chart"**

## 📁 Project Structure

```
berc_grapher/
│
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
│
├── gui/                    # GUI components
│   ├── __init__.py
│   ├── main_window.py      # Main application window
│   ├── file_panel.py       # Excel file loading interface
│   ├── style_panel.py      # Style and appearance controls
│   ├── axis_panel.py       # Axis configuration controls
│   └── export_panel.py     # Export settings and actions
│
├── engine/                 # Chart generation engine
│   ├── __init__.py
│   ├── chart_engine.py     # Matplotlib rendering engine
│   └── config_builder.py   # Configuration data structures
│
├── utils/                  # Utility modules
│   ├── __init__.py
│   └── excel_reader.py     # Excel file reading and parsing
│
└── assets/                 # Assets and resources
    ├── __init__.py
    └── themes.py           # Predefined color themes
```

## 🏗️ Architecture

The application follows a clean separation of concerns:

```
GUI Layer (PySide6)
    ↓
Configuration Builder
    ↓
Chart Engine (matplotlib)
    ↓
Output (Preview/Export)
```

### Key Design Principles

1. **Separation of Concerns**: GUI components never directly manipulate matplotlib
2. **Configuration Objects**: All settings pass through typed configuration classes
3. **Signal-Based Updates**: Qt signals coordinate between components
4. **Debounced Rendering**: Prevents performance issues during rapid changes

## 🎨 Available Themes

- **Light**: Classic white background with standard colors
- **Dark**: Dark background for reduced eye strain
- **Scientific**: Professional color scheme for academic publications
- **Vibrant**: Bold, eye-catching colors for presentations
- **Pastel**: Soft, muted colors for gentle visualizations
- **Monochrome**: Grayscale palette for print compatibility

## 💡 Tips and Best Practices

### For Best Results

1. **Data Preparation**: Ensure your Excel data has:
   - Clear column headers
   - Consistent data types
   - No merged cells in data range

2. **Column Selection**: 
   - Use numeric columns for Y-axis
   - X-axis can be text or numeric

3. **Secondary Y-Axis**:
   - Use when Y values have very different scales
   - Label clearly to avoid confusion

4. **Export Quality**:
   - Use 300 DPI for printed materials
   - Use SVG or PDF for publications requiring vector graphics
   - Use 72 DPI for web/screen display

5. **Color Selection**:
   - Ensure sufficient contrast for readability
   - Consider colorblind-friendly palettes
   - Test prints in grayscale if needed

## 🔧 Troubleshooting

### Application won't start
- Verify Python version: `python --version` (must be 3.8+)
- Ensure all dependencies installed: `pip list`
- Try reinstalling: `pip install -r requirements.txt --force-reinstall`

### Excel file won't load
- Check file format (.xlsx, .xls, .xlsm)
- Ensure file isn't open in Excel
- Verify file isn't corrupted

### Preview not updating
- Check that both X and Y columns are selected
- Verify data contains valid numeric values
- Look for error messages in status bar

### Export fails
- Ensure you have write permissions to output directory
- Check that output path doesn't contain invalid characters
- Verify sufficient disk space

## 📊 Example Use Cases

### Research Data
- Plot experimental results with error bars
- Compare multiple treatment groups
- Create publication-ready figures

### Business Analytics
- Visualize sales trends over time
- Compare metrics across departments
- Generate report charts

### Academic Projects
- Analyze survey data
- Display statistical results
- Create presentation graphics

## 🛠️ Development

### Adding New Themes

Edit `assets/themes.py`:

```python
THEMES['MyTheme'] = {
    'background': '#FFFFFF',
    'grid': '#CCCCCC',
    'text': '#000000',
    'axis': '#000000',
    'line_colors': ['#color1', '#color2', ...]
}
```

### Extending Export Formats

Add format support in `engine/chart_engine.py`:

```python
valid_formats = ['png', 'svg', 'pdf', 'eps']  # Add 'eps'
```

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 👥 Credits

**Developed by**: BERC (Business and Economic Research Center)  
**Version**: 1.0.0  
**Python**: 3.8+  
**Framework**: PySide6 (Qt for Python)  
**Visualization**: matplotlib

## 🤝 Support

For issues, questions, or suggestions:
- Check the Troubleshooting section above
- Review error messages in the application status bar
- Verify your data format matches requirements

## 🔄 Version History

### Version 1.0.0 (Current)
- Initial release
- Full Excel file support
- Six preset themes
- PNG, SVG, PDF export
- Dual Y-axis support
- Live preview
- Comprehensive customization options

---

**Note**: This is production-ready software designed for professional use in research, business, and academic environments.
