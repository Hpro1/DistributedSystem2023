from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = password
    return jsonify({"success": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    if users[username] != password:
        return jsonify({"error": "Invalid password"}), 401

    # Ideally, generate and return a secure token for authentication
    return jsonify({"success": "Logged in"}), 200

if __name__ == '__main__':
    app.run(debug=True)
