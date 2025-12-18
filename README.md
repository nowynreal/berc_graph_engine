# Excel Chart Generator

A professional desktop GUI application for creating highly customizable charts from Excel data files. Built with PySide6 (Qt) and matplotlib, this tool provides researchers and analysts with a powerful, user-friendly interface for publication-ready data visualization.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎯 Features

### Data Loading & Management
- **Excel File Support**: Load `.xlsx`, `.xls`, and `.xlsm` files
- **Sheet Selection**: Choose from multiple worksheets with live data preview
- **Smart Column Mapping**: Intuitive table-based column selection with Y1/Y2 assignment
- **Auto-Label Detection**: Automatically suggests axis labels from column names
- **Dual Y-Axis**: Support for secondary Y-axis with independent scaling and auto-enable
- **Column Preview**: View data before plotting with sortable tables

### Advanced Chart Customization

#### Professional Style Profiles (Unified System - 10 Presets)
Comprehensive style profiles that combine colors, typography, grid settings, and layout in one click:

- **IMF Official**: International Monetary Fund publication style
- **World Bank Report**: World Bank official reports and publications
- **Professional Clean**: Classic business presentation with horizontal gridlines
- **Analytical Grid**: Value-reading focused with vertical gridlines
- **Academic Journal**: Serif fonts for academic publications
- **Presentation**: Bold, modern style for slide presentations
- **Minimal Grid**: Lightweight design with subtle gridlines
- **Full Grid**: Comprehensive reference grids on both axes
- **No Grid**: Clean, distraction-free style
- **Dark Mode**: Modern dark theme for reduced eye strain

Each style includes:
✓ Optimized color palette (10 colors per profile)
✓ Grid type and styling (X-only, Y-only, both, or none)
✓ Typography (font family, size, title weight)
✓ Legend positioning and transparency
✓ Professional axis and text colors

#### Style Controls (Tabbed Interface)
- **General Tab**:
  - **Professional Style Selector**: 10 unified style profiles (IMF, World Bank, Academic, Presentation, etc.)
  - **Colors**: Fine-tune background and grid colors
  - **Typography**: Font family selection (20+ fonts), sizes for text and titles
  - **Grid Control**: Choose grid configuration:
    - X Axis Only (horizontal lines) - publication style
    - Y Axis Only (vertical lines) - analytical reading
    - Both Axes - comprehensive reference
    - No Grid - clean appearance
  - **Real-time Customization**: Override any style setting
- **Special Scenarios**:
  - COVID-19 period highlighting (2020-2021)
  - Great Recession (2008-2009)
  - Housing Crisis (2007-2012)
  - Interest Rate Hikes (2022-2023)
  - Custom period overlays with transparency and labels
- **Legend Tab**:
  - Position control (best, upper/lower right/left, center)
  - Multi-column layout (1-4 columns)
  - Custom legend title
  - Frame transparency control
  - Spacing adjustments (label spacing, handle length, text padding)
- **Lines Tab**:
  - Individual line customization per data series
  - Color pickers for each line
  - Line styles: Solid, dashed, dotted, dash-dot
  - Line width: Adjustable from 0.5 to 10.0 pixels
  - Markers: Circle, square, triangle, diamond, plus, cross, or none
  - Y2 axis assignment per line
  - **Smoothing**: Moving average with configurable window (1-25 points)
  - **Premium Rendering**: Round line caps/joins and antialiasing for professional appearance

#### Axis Configuration (Tabbed Interface)
- **Titles Tab**:
  - Main chart title with alignment (left/center/right) and vertical offset
  - Optional subtitle with 5 alignment modes:
    - Chart-based: Left/Center/Right (relative to chart area)
    - Figure-based: Left/Right (relative to canvas edges)
  - Subtitle positioned relative to title (negative offset = below)
  - Bold toggle and size control for both titles
- **X-Axis, Y1-Axis, Y2-Axis Tabs**:
  - Custom axis labels with bold option
  - Min/Max value ranges (auto-scale or manual)
  - Tick rotation (-90° to +90°)
  - Tick step control for custom intervals
  - Categorical mode (preserve all labels)
  - Grouped categorical (e.g., "2006 q1" → show only "2006")
  - Hide labels option (keep grid/ticks, suppress labels)
  - Scale selection (Linear or Log)
  - Value format: Auto, Decimal, Scientific, Percent, Integer
- **Figure Tab**:
  - Width: 4-20 inches
  - Height: 3-15 inches

### Live Preview & Performance
- **Real-time Updates**: See changes instantly with 300ms debounce
- **Embedded Preview**: No need to export to see results
- **Smart Rendering**: Efficient chart updates during configuration

### Export Options
- **PNG Export**: High-quality raster images with adjustable DPI (72-600)
  - Screen quality: 72 DPI
  - Draft quality: 150 DPI
  - Print quality: 300 DPI
  - High quality: 600 DPI
- **SVG Export**: Scalable vector graphics for publications
- **PDF Export**: Professional documents ready for printing
- **File Browser**: Easy output location selection
- **Tight Layout**: Automatic bbox optimization

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

#### 2. Map Columns
1. Use the **Column Mapping** table to assign roles:
   - Click **X** radio button for your X-axis column
   - Click **Y-1** checkboxes for primary Y-axis columns
   - Click **Y-2** checkboxes for secondary Y-axis columns
2. Selected columns appear in the **Current Selection** summary
3. Y2 axis is automatically enabled when Y-2 columns are selected
4. Axis labels are auto-suggested from column names

#### 3. Customize Style
1. Click the **"Style"** tab
2. **General Tab**:
   - Choose a preset theme (22+ options including colorblind-safe)
   - Select special scenario highlighting (COVID-19, Recessions, etc.)
   - Adjust background, grid, and font settings
3. **Legend Tab**:
   - Configure position, columns, title, and spacing
4. **Lines Tab**:
   - Customize each line's color, style, width, and markers
   - Apply smoothing (moving average with 1-25 point window)
   - Assign lines to Y2 axis individually

#### 4. Configure Axes
1. Click the **"Axes"** tab
2. **Titles Tab**:
   - Set main title with alignment and offset
   - Add optional subtitle with chart/figure-based alignment
3. **X-Axis, Y1-Axis, Y2-Axis Tabs**:
   - Labels are auto-filled from mapping (editable)
   - Set min/max ranges or leave auto
   - Adjust tick rotation, step, and format
   - Enable categorical or grouped modes
4. **Figure Tab**:
   - Set canvas dimensions (width/height in inches)

#### 5. Preview & Export
- Chart updates live in the preview panel
- Click **"Export"** tab when ready
- Choose format (PNG/SVG/PDF) and quality
- Click **"Export Chart"**

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

### Standard Themes
- **Light**: Classic white background with standard colors
- **Dark**: Dark background for reduced eye strain with bright, visible colors
- **Scientific**: Professional serif fonts and academic color palette
- **Vibrant**: Bold, eye-catching Material Design colors
- **Pastel**: Soft, muted colors for gentle visualizations
- **Monochrome**: Grayscale palette for print compatibility
- **Publication**: Black/red/blue academic palette with serif fonts

### MTSU Branded Themes
- **MTSU Blue**: Official MTSU dark blue, bright blue, and orange
- **MTSU Bold**: High-contrast red/blue for presentations
- **MTSU Publication**: Academic publication style with Times New Roman

### BERC Professional Themes
- **BERC Professional**: Navy-to-teal gradient palette
- **BERC Report**: Red/blue report style with Arial
- **BERC Dark**: Dark mode with vibrant accent colors
- **BERC Nashville**: High-contrast presentation theme
- **BERC Modern**: Dodger blue/tomato modern palette
- **BERC Corporate**: Times New Roman with Excel-inspired colors

### Premium Design Themes
- **Carbon Modern**: Dark technology theme (Segoe UI, indigo/aqua/amber)
- **Nordic Calm**: Scandinavian-inspired calm palette (Calibri, blue/teal/sage)
- **Sandstone Editorial**: Warm editorial design (Georgia, burnt umber/slate)
- **Indigo Print**: Publication-quality indigo theme (Garamond, royal blue/salmon)
- **Aurora Tech**: Neon cyberpunk aesthetics (Roboto, cyan/purple/mint)
- **Evergreen Atlas**: Natural earth tones (Palatino, evergreen/gold/steel)

### Accessibility
- **Accessible (Colorblind Safe)**: Okabe-Ito palette designed for protanopia, deuteranopia, and tritanopia color vision deficiencies. Ensures charts are readable for all users.

## 💡 Tips and Best Practices

### For Best Results

1. **Data Preparation**: Ensure your Excel data has:
   - Clear column headers
   - Consistent data types
   - No merged cells in data range

2. **Column Selection**: 
   - Use numeric columns for Y-axis
   - X-axis can be text or numeric
   - Use Column Mapping table for precise control

3. **Secondary Y-Axis**:
   - Use when Y values have very different scales
   - Automatically enabled when Y-2 columns are mapped
   - Labels auto-suggested from column names

4. **Themes & Accessibility**:
   - Dark themes automatically adjust text/axis colors for visibility
   - Use "Accessible (Colorblind Safe)" for universal readability
   - Test theme contrast before exporting

5. **Smoothing**:
   - Apply moving average (1-25 window) for noisy data
   - Larger windows = smoother lines but less detail
   - Preview changes before exporting

6. **Period Highlights**:
   - Use Special Scenarios for common economic/pandemic periods
   - Highlights align to year-based x-axis data
   - Combine with themes for professional context

7. **Export Quality**:
   - Use 300 DPI for printed materials
   - Use SVG or PDF for publications requiring vector graphics
   - Use 72 DPI for web/screen display

8. **Title & Subtitle**:
   - Subtitle offset is relative to title (negative = below)
   - Use chart-based alignment for consistent positioning
   - Use figure-based for edge-aligned annotations

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
**Version**: 2.0.0  
**Release Date**: December 2025  
**Python**: 3.8+  
**Framework**: PySide6 (Qt for Python)  
**Visualization**: matplotlib  
**Accessibility**: Okabe-Ito colorblind-safe palette

## 🤝 Support

For issues, questions, or suggestions:
- Check the Troubleshooting section above
- Review error messages in the application status bar
- Verify your data format matches requirements

## 🔄 Version History

### Version 2.0.0 (Current - December 2025)
**Major UI/UX Overhaul & Professional Design Features**

#### Interface Improvements
- **Tabbed Panels**: Organized Style (General/Legend/Lines) and Axes (Titles/X/Y1/Y2/Figure) into tabs
- **Column Mapping Table**: Intuitive radio/checkbox table for X/Y1/Y2 assignment
- **Auto-Label & Enable**: Y2 axis labels auto-suggested and enabled from column mapping
- **Smart Filtering**: Column mapping table with role filter

#### Advanced Styling
- **16 New Themes**: MTSU branded, BERC professional, premium modern designs
- **Colorblind Safe**: Accessible theme using Okabe-Ito palette
- **Theme Intelligence**: Automatic text/axis color adaptation to background
- **Font Expansion**: 20+ font families with fallback handling
- **Premium Rendering**: Round line caps/joins, antialiasing for smooth appearance

#### Chart Features
- **Line Smoothing**: Moving average with configurable 1-25 point window
- **Period Highlights**: Special scenario presets (COVID-19, recessions) with year-based alignment
- **Subtitle System**: 5 alignment modes (chart/figure-based) with relative positioning
- **Categorical Axes**: Grouped labels (e.g., quarterly → yearly), hide labels option
- **Enhanced Legend**: Multi-column, title, spacing, transparency controls

#### Technical Enhancements
- **Font Fallback**: Automatic fallback for missing fonts (Roboto → Segoe UI/Arial/Calibri)
- **Dark Theme Support**: Full x-axis tick label color synchronization
- **Y2 Auto-Enable**: Secondary axis automatically enabled when Y2 columns mapped
- **Config Extensibility**: Text color, smoothing, period highlights in ChartConfig

### Version 1.0.0 (Initial Release)
- Full Excel file support
- Six preset themes
- PNG, SVG, PDF export
- Dual Y-axis support
- Live preview
- Basic customization options

---

**Note**: This is production-ready software designed for professional use in research, business, and academic environments.
