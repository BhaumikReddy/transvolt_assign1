# Voltage Data Analysis Flask Web App

A comprehensive web dashboard for analyzing voltage data with interactive charts and statistical insights, optimized for PythonAnywhere deployment.

## Features

- **Interactive Voltage Plots**: Real-time voltage data visualization
- **Moving Average Analysis**: 5-sample, 1000-sample, and 5000-sample moving averages
- **Peak & Valley Detection**: Automatic identification of voltage extremes
- **Statistical Dashboard**: Key metrics and data insights
- **Responsive Design**: Professional web interface with Bootstrap styling

## Files Structure

```
webapp_deployment/
├── app.py                 # Main Flask application
├── flask_app.py          # WSGI file for PythonAnywhere
├── requirements.txt      # Python dependencies
├── Sample_Data.csv       # Voltage data file
├── voltage_analysis.py   # Standalone analysis script
├── templates/
│   └── index.html        # Web dashboard template
└── README.md            # This file
```

## Deployment on PythonAnywhere

### Step 1: Upload Files to PythonAnywhere
1. Create a free account at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Go to your Dashboard → Files
3. Upload all files from the `webapp_deployment` folder to your home directory
4. Alternatively, clone from GitHub if you've uploaded there

### Step 2: Install Dependencies
1. Open a Bash console from your Dashboard
2. Navigate to your project directory:
   ```bash
   cd ~/webapp_deployment
   ```
3. Install required packages:
   ```bash
   pip3.10 install --user -r requirements.txt
   ```

### Step 3: Configure Web App
1. Go to Dashboard → Web
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. In the "Code" section:
   - **Source code**: `/home/yourusername/webapp_deployment`
   - **Working directory**: `/home/yourusername/webapp_deployment`
   - **WSGI configuration file**: Click to edit and replace content with:

```python
import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/webapp_deployment'  # Replace 'yourusername' with your actual username
if path not in sys.path:
    sys.path.append(path)

from app import app as application

if __name__ == "__main__":
    application.run()
```

### Step 4: Configure Static Files (Optional)
In the "Static files" section, you can add:
- URL: `/static/`
- Directory: `/home/yourusername/webapp_deployment/static/`

### Step 5: Launch Your App
1. Click "Reload" button at the top of the Web tab
2. Your app will be available at: `https://yourusername.pythonanywhere.com`

## GitHub Upload Instructions

### To upload this project to GitHub:

1. **Create a new repository** on GitHub
2. **Initialize git** in your local webapp_deployment folder:
   ```bash
   cd webapp_deployment
   git init
   git add .
   git commit -m "Initial commit: Voltage analysis Flask app for PythonAnywhere"
   ```
3. **Connect to GitHub**:
   ```bash
   git remote add origin https://github.com/yourusername/voltage-analysis-app.git
   git branch -M main
   git push -u origin main
   ```

### Deploy from GitHub to PythonAnywhere:
1. In PythonAnywhere Bash console:
   ```bash
   git clone https://github.com/yourusername/voltage-analysis-app.git
   cd voltage-analysis-app
   pip3.10 install --user -r requirements.txt
   ```

## Local Development

To run locally:

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to view the dashboard.

## Data Analysis Features

### Charts Available:
1. **Basic Voltage Plot**: Raw voltage data over time
2. **Moving Average Overlay**: 5-sample moving average comparison
3. **Advanced Moving Averages**: 1000 and 5000 sample comparisons

### Statistics Displayed:
- Total data points
- Voltage peaks and valleys count
- Values below 20V threshold
- Min, max, and average voltage

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure all packages are installed via pip
2. **File Path Issues**: Ensure `Sample_Data.csv` is in the same directory as `app.py`
3. **WSGI Errors**: Check that the path in `flask_app.py` matches your actual directory
4. **Memory Issues**: For large datasets, consider data sampling or chunking

### PythonAnywhere Specific:
- Use the correct Python version (3.10 recommended)
- Install packages with `--user` flag
- Check error logs in the Web tab if the app doesn't load
- Make sure the WSGI file path matches your username and directory structure

## Assignment Requirements Completed ✅

- **Task 3**: Python code hosted on web (no Streamlit)
- **Task 4**: Web app with all charts combined in one dashboard
- **Free hosting**: Ready for PythonAnywhere deployment
- **Professional interface**: Bootstrap-styled responsive design
- **All analysis features**: Moving averages, peak detection, statistics

## License

This project is created for educational purposes as part of Assignment 1.

## Support

For issues with deployment, check:
- PythonAnywhere help documentation
- Flask official documentation  
- Plotly documentation for chart customization
