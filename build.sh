#!/bin/bash
set -o errexit

echo "=== Build Debug Info ==="
echo "Current directory: $(pwd)"
echo "Contents of current directory:"
ls -la
echo "Contents of backend directory:"
ls -la backend/ || echo "backend directory not found"
echo "Contents of your_application directory:"
ls -la your_application/ || echo "your_application directory not found"

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Ensure Python path is set correctly
export PYTHONPATH="$(pwd):${PYTHONPATH}"
echo "PYTHONPATH: $PYTHONPATH"

# Test imports that gunicorn will need
echo "Testing your_application import..."
python -c "import sys; sys.path.insert(0, '.'); import your_application; print('✓ your_application imported successfully')" || echo "✗ your_application import failed"

echo "Testing your_application.wsgi import..."
python -c "import sys; sys.path.insert(0, '.'); from your_application.wsgi import application; print('✓ WSGI application loaded successfully')" || echo "✗ WSGI application load failed"

echo "Testing backend main.py import..."
python -c "import sys; sys.path.insert(0, './backend'); from main import app; print('✓ Backend app imported successfully')" || echo "✗ Backend app import failed"

echo "=== Build completed successfully ==="