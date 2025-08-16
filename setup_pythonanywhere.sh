#!/bin/bash
# PythonAnywhere Deployment Setup Script
# Run this script in PythonAnywhere Bash console after uploading files

echo "Setting up Voltage Analysis Flask App for PythonAnywhere..."

# Create virtual environment (optional but recommended)
# mkvirtualenv --python=/usr/bin/python3.10 voltage-app

# Install requirements
echo "Installing Python packages..."
pip3.10 install --user -r requirements.txt

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Go to Web tab in PythonAnywhere dashboard"
echo "2. Create new web app (Manual configuration, Python 3.10)"
echo "3. Set source code path to: /home/yourusername/webapp_deployment"
echo "4. Edit WSGI file and paste the configuration from README.md"
echo "5. Reload your web app"
echo ""
echo "Your app will be available at: https://yourusername.pythonanywhere.com"
