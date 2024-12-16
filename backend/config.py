import os

class Config:
    FLASK_HOST = os.environ.get('FLASK_HOST', 'localhost')
    FLASK_PORT = os.environ.get('FLASK_PORT', '5000')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)