from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api/data')
def get_data():
    print("hewwo world")
    return jsonify({"message": "Hello from our new new Flask backend!"})

if __name__ == '__main__':
    app.run(
        debug=Config.FLASK_DEBUG, 
        host=Config.FLASK_HOST, 
        port=Config.FLASK_PORT
    )