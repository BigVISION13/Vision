from flask import Flask, request, jsonify
from vision.response_generator import generate_response

app = Flask(__name__)

@app.route('/generate-response', methods=['POST'])
def generate_response_route():
    data = request.get_json(silent=True) or {}
    context = data.get('context')
    style = data.get('style')
    generated = generate_response(context, style)
    return jsonify({"response": generated})

if __name__ == '__main__':
    app.run(debug=True)

