#!/bin/bash
# Startup wrapper for Render deployment

echo "=== Starting Tutor Agent ==="
echo "Current directory: $(pwd)"
echo "Contents: $(ls -la)"

# Set Python path to include current directory
export PYTHONPATH="$(pwd):${PYTHONPATH}"
echo "PYTHONPATH: $PYTHONPATH"

# Test if we can import the application
echo "Testing application import..."
python -c "from your_application.wsgi import application; print('Application ready')" || {
    echo "Application import failed, trying direct startup..."
    exec python start_server.py
}

# If import works, let gunicorn handle it
echo "Starting with gunicorn..."
exec gunicorn your_application.wsgi --bind 0.0.0.0:$PORT --workers 2