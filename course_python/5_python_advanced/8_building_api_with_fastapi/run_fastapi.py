import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.getcwd())

try:
    # Import the FastAPI app using the correct module path
    # We need to use importlib to handle the directory structure
    import importlib.util
    import pathlib
    
    # Get the path to the main.py file
    main_path = pathlib.Path("course_python/5_python_advanced/8_building_api_with_fastapi/main.py")
    
    # Load the module
    spec = importlib.util.spec_from_file_location("main", main_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    
    # Get the app from the module
    app = main_module.app
    
    # Run the app using uvicorn programmatically
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure FastAPI and uvicorn are installed:")
    print("pip install fastapi uvicorn")
except Exception as e:
    print(f"Error: {e}")
