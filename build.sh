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

pip install --upgrade pip
pip install -r requirements.txt

# Ensure your_application is importable
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
echo "Testing your_application import..."
python -c "import your_application; print('your_application imported successfully')"
echo "Testing your_application.wsgi import..."
python -c "from your_application.wsgi import application; print('WSGI application loaded successfully')"
echo "=== Build completed successfully ==="