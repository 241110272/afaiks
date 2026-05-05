#!/usr/bin/env python
"""
AFAIKs - Smart Collaborative To-Do List
Quick startup script with setup wizard
"""

import os
import sys
from pathlib import Path


def check_env_file():
    """Check if .env file exists, create from example if not"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            print("Creating .env file from .env.example...")
            with open('.env.example', 'r') as f:
                content = f.read()
            with open('.env', 'w') as f:
                f.write(content)
            print("✓ .env file created. Please update with your settings.")
        else:
            print("⚠ .env.example not found. Please create .env file manually.")
    else:
        print("✓ .env file found")


def check_requirements():
    """Check if all requirements are installed"""
    try:
        import flask
        import flask_login
        import flask_wtf
        import flask_sqlalchemy
        import reportlab
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nTo install dependencies, run:")
        print("  pip install -r requirements.txt")
        return False


def create_database():
    """Create database tables"""
    try:
        from app import create_database as create_db
        print("✓ Initializing database...")
        create_db()
        print("✓ Database ready")
    except Exception as e:
        print(f"✗ Error creating database: {e}")


def main():
    """Main startup function"""
    print("\n" + "="*50)
    print("AFAIKs - Smart Collaborative To-Do List")
    print("="*50 + "\n")
    
    # Check environment setup
    print("Checking environment setup...")
    check_env_file()
    print()
    
    # Check dependencies
    print("Checking dependencies...")
    if not check_requirements():
        sys.exit(1)
    print()
    
    # Initialize database
    print("Initializing application...")
    create_database()
    print()
    
    # Start the application
    print("="*50)
    print("Starting AFAIKs server...")
    print("="*50)
    print("\nApplication will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        from app import app
        app.run(debug=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)


if __name__ == '__main__':
    main()
