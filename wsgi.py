"""
WSGI entry point for production deployment
"""
from app import app, create_database

# Initialize database once when the app starts
create_database()

if __name__ == "__main__":
    app.run()
