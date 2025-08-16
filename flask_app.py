"""
WSGI Configuration for PythonAnywhere
This file is required for PythonAnywhere Flask deployment
"""

# WSGI configuration file for PythonAnywhere
import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/mysite'  # Update this path when you upload to PythonAnywhere
if path not in sys.path:
    sys.path.append(path)

from app import app as application

if __name__ == "__main__":
    application.run()
