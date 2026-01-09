from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_emotion = {
    "emotion": "neutral",
    "confidence": 0.0
}

@app.route("/emotion", methods=["POST"])
def receive_audio():
    global latest_emotion

    audio_data = request.data
    print("Received audio bytes:", len(audio_data))

    latest_emotion = {
        "emotion": "happy",
        "confidence": 0.87
    }

    return jsonify(latest_emotion)

@app.route("/latest-emotion", methods=["GET"])
def latest():
    return jsonify(latest_emotion)

@app.route("/")
def home():
    return "MoodMate Backend Running"
