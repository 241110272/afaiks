"""
WSGI entry point for production deployment
"""
from app import app, create_database

# Initialize database on first request
@app.before_request
def init_db():
    create_database()

if __name__ == "__main__":
    app.run()
