"""
WSGI entry point for production deployment
"""
from app import app, create_database

# Initialize database
create_database()

if __name__ == "__main__":
    app.run()
