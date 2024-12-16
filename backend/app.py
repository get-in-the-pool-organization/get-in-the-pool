from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

#pee pee poopoo poo poo 
@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from our new new Flask backend!"})

if __name__ == '__main__':
    app.run(debug=True)