# 🧪 β-Galactosidase Assay Calculator

A mobile-friendly Streamlit web application for calculating solution volumes and protocols for β-galactosidase staining assays. This tool helps researchers quickly determine the exact amounts of reagents needed for different culture plate formats.

## ✨ Features

- **Mobile-Optimized Design**: Responsive layout designed specifically for mobile web browsers
- **Dark Mode Support**: Automatic theme detection with full dark mode compatibility
- **Multiple Plate Types**: Support for 6-well, 12-well, 24-well plates, and 100π dishes
- **Real-Time Calculations**: Instant volume calculations based on plate type and well count
- **Solution Breakdown**: Detailed reagent volumes for all required solutions
- **Protocol Display**: Step-by-step protocol with calculated volumes
- **Quick Reference**: Summary of total volumes needed

## 🔬 Supported Plate Types

| Plate Type | Area (cm²) | Media Volume (ml) | Working Volume (ml) |
|------------|------------|-------------------|---------------------|
| 6-well     | 9.6        | 2.0               | 1.0                 |
| 12-well    | 3.5        | 1.0               | 0.5                 |
| 24-well    | 1.9        | 0.5               | 0.25                |
| 100π dish  | 56.7       | 8.0               | 4.0                 |

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd beta-gal-calculator
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit
   ```

3. **Run the application**
   ```bash
   streamlit run beta_gal_app.py
   ```

4. **Access the app**
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

## 📱 Mobile Usage

This app is specifically optimized for mobile web browsers:

1. **Open your mobile browser** (Chrome, Safari, Firefox, etc.)
2. **Navigate to the app URL**
3. **Select your plate type** from the dropdown
4. **Enter the number of wells/dishes**
5. **View calculated volumes** in expandable sections
6. **Access the protocol** when needed

## 🧪 Solutions Calculated

The app calculates volumes for three essential solutions:

### 1. 1X PBS Solution
- **Components**: 10X PBS stock + Distilled water
- **Usage**: Three rinses during the protocol
- **Ratio**: 1:9 (stock:water)

### 2. 1X Fixative Solution
- **Components**: 10X Fixative Solution + Distilled water
- **Usage**: Cell fixation step
- **Ratio**: 1:9 (stock:water)

### 3. β-Galactosidase Staining Solution
- **Components**:
  - 10X Staining Solution
  - 100X Solution A
  - 100X Solution B
  - X-gal powder
  - DMSO
  - Distilled water

## 🎨 Theme Support

The app automatically adapts to your device's theme preference:

- **Light Mode**: Clean, bright interface for normal lighting
- **Dark Mode**: Easy on the eyes for low-light conditions
- **Auto-Detection**: Follows system preferences automatically

## 📋 Protocol Overview

The generated protocol includes these steps:

1. Remove growth media
2. PBS rinse (1x)
3. Add fixative solution
4. Room temperature incubation (10-15 min)
5. PBS rinse (2x)
6. Add staining solution
7. Seal with parafilm
8. Overnight incubation at 37°C

## 🛠️ Technical Details

### Built With
- **Streamlit**: Web app framework
- **Python**: Backend logic and calculations
- **CSS**: Custom styling for mobile optimization and dark mode

### Architecture
- **Object-Oriented Design**: Separate classes for each plate type
- **Inheritance**: Base `beta_gal_assay` class with specialized subclasses
- **Responsive CSS**: Mobile-first design approach

### File Structure
```
├── beta_gal_app.py          # Main Streamlit application
├── README.md                # This file
└── requirements.txt         # Dependencies (optional)
```

## 🧬 Scientific Background

β-galactosidase staining is a widely used technique in molecular biology for:
- **Gene Expression Analysis**: Visualizing lacZ reporter gene activity
- **Cell Lineage Tracing**: Tracking cell fate in development
- **Senescence Detection**: Identifying senescent cells
- **Transgenic Studies**: Confirming successful gene integration

## 🔧 Customization

To modify plate specifications or add new plate types:

1. **Create a new class** inheriting from `beta_gal_assay`
2. **Set the plate parameters**:
   ```python
   class custom_plate(beta_gal_assay):
       def __init__(self, num_of_wells):
           super().__init__(num_of_wells)
           self.area = X.X        # cm²
           self.media_volume = X  # ml
           self.working_volume = self.media_volume / 2  # ml
   ```
3. **Add to the options dictionary** in the main function

## 📊 Example Calculations

For a **6-well plate** with **3 wells**:

- **PBS Total**: 18.0 ml (for 3 rinses)
- **Fixative Total**: 3.0 ml  
- **Staining Total**: 3000 μl

## 🐛 Troubleshooting

### Common Issues

**App won't start**
- Check Python version (3.7+)
- Ensure Streamlit is installed: `pip install streamlit`

**Styling issues on mobile**
- Clear browser cache
- Try refreshing the page
- Check if JavaScript is enabled

**Dark mode not working**
- Verify browser supports CSS `prefers-color-scheme`
- Try manually toggling Streamlit's theme

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by **davis_k**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📞 Support

For questions or support, please create an issue in the repository.

---

*Happy researching! 🧪✨*
