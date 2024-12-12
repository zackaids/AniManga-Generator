from flask import Flask, request, jsonify
from fetch_data import fetch_anime_data
from model import generate_summary

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    genre = data['genre']
    summary = generate_summary(genre)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
