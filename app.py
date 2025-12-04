#!/usr/bin/env python3
"""
Alternative WSGI entry point for Render deployment
"""
import os
import sys

# Add backend to path
backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
sys.path.insert(0, backend_path)

print(f"Loading app from: {backend_path}")
print(f"Python path: {sys.path}")

from main import app

# For gunicorn
application = app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)