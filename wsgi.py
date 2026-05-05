"""
WSGI entry point for production deployment
"""
from app import app, create_database

# Initialize database once when the app starts
try:
    create_database()
except Exception as e:
    app.logger.error(f"Database initialization failed: {e}")

if __name__ == "__main__":
    app.run()
