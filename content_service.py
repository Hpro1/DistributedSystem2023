from flask import Flask, request, jsonify

app = Flask(__name__)

contents = []

@app.route('/content', methods=['POST'])
def create_content():
    content = request.json
    contents.append(content)
    return jsonify({"success": "Content created"}), 201

@app.route('/content', methods=['GET'])
def get_contents():
    return jsonify(contents)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
