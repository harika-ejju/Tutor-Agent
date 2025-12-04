#!/bin/bash
set -o errexit

# Disable Rust compilation completely
export CARGO_NET_OFFLINE=true
export PYO3_NO_PYTHON_VERSION_CHECK=1
export RUSTUP_TOOLCHAIN=

pip install --upgrade pip

# Install each package individually to identify which one fails
pip install --no-cache-dir --only-binary=:all: fastapi==0.88.0
pip install --no-cache-dir --only-binary=:all: uvicorn==0.20.0
pip install --no-cache-dir --only-binary=:all: starlette==0.22.0
pip install --no-cache-dir --only-binary=:all: pydantic==1.9.2
pip install --no-cache-dir --only-binary=:all: redis==4.3.4
pip install --no-cache-dir --only-binary=:all: requests==2.28.2
pip install --no-cache-dir --only-binary=:all: python-dotenv==0.19.2
pip install --no-cache-dir --only-binary=:all: gunicorn==20.1.0