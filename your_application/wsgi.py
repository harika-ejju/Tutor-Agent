"""
Simplified WSGI module for gunicorn deployment
"""
import os
import sys

print(f"=== WSGI Module Loading ===")
print(f"File: {__file__}")
print(f"Working directory: {os.getcwd()}")
print(f"Directory contents:")
try:
    contents = os.listdir('.')
    for item in contents[:10]:  # Show first 10 items
        print(f"  {item}")
except:
    print("  Could not list directory")

# Add paths more aggressively
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.join(current_dir, 'backend')

print(f"Current dir: {current_dir}")
print(f"Backend dir: {backend_dir}")

# Insert at beginning of path
sys.path.insert(0, backend_dir)
sys.path.insert(0, current_dir)

print(f"Updated Python path (first 3): {sys.path[:3]}")

# Try multiple import strategies
application = None

# Strategy 1: Direct import from main
try:
    print("Strategy 1: Importing from main...")
    from main import app
    application = app
    print("✓ Success: Imported from main")
except Exception as e:
    print(f"✗ Failed: {e}")

# Strategy 2: Import after changing directory
if application is None:
    try:
        print("Strategy 2: Changing to backend directory...")
        original_cwd = os.getcwd()
        os.chdir(backend_dir)
        from main import app
        application = app
        os.chdir(original_cwd)
        print("✓ Success: Imported after directory change")
    except Exception as e:
        print(f"✗ Failed: {e}")
        # Restore directory
        try:
            os.chdir(original_cwd)
        except:
            pass

# Strategy 3: Fallback FastAPI app
if application is None:
    print("Strategy 3: Creating fallback application...")
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        
        app = FastAPI(title="Tutor Agent Fallback", version="1.0.0")
        
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        @app.get("/")
        async def fallback_root():
            return {"message": "Tutor Agent API (Fallback Mode)", "status": "limited_functionality"}
            
        @app.get("/health")
        async def fallback_health():
            return {"status": "healthy", "mode": "fallback"}
        
        application = app
        print("✓ Success: Created fallback application")
    except Exception as e:
        print(f"✗ Failed to create fallback: {e}")
        raise

print(f"=== WSGI Module Ready ===")
print(f"Application: {application}")
print(f"Application type: {type(application)}")