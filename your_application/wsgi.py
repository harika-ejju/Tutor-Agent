"""
WSGI module for gunicorn deployment
"""
import os
import sys

# Print debug info
print(f"WSGI module loading from: {__file__}")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Add paths
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.join(current_dir, 'backend')

paths_to_add = [current_dir, backend_dir]
for path in paths_to_add:
    if path not in sys.path:
        sys.path.insert(0, path)
        print(f"Added to Python path: {path}")

print(f"Updated Python path: {sys.path}")

try:
    # Import the FastAPI application
    from main import app
    application = app
    print("✓ FastAPI application loaded successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Files in backend directory:")
    try:
        backend_files = os.listdir(backend_dir)
        print(backend_files)
    except:
        print("Cannot list backend directory")
    raise