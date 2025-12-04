#!/usr/bin/env python3
"""
Direct startup script to bypass gunicorn issues
"""
import os
import sys

# Add paths
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'backend')

sys.path.insert(0, current_dir)
sys.path.insert(0, backend_dir)

# Change to backend directory
os.chdir(backend_dir)

print(f"Working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Import and run
from main import app
import uvicorn

port = int(os.environ.get("PORT", 8000))
print(f"Starting Tutor Agent on port {port}")

uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")