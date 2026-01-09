from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

latest_emotion = {
    "emotion": "neutral",
    "confidence": 0.0
}

@app.route("/emotion", methods=["POST"])
def receive_emotion():
    global latest_emotion

    audio_data = request.data
    print("Received audio bytes:", len(audio_data))

    emotions = ["happy", "sad", "angry", "neutral", "surprised"]

    latest_emotion = {
        "emotion": random.choice(emotions),
        "confidence": round(random.uniform(0.6, 0.95), 2)
    }

    return jsonify({"status": "received"}), 200


@app.route("/latest-emotion", methods=["GET"])
def get_latest_emotion():
    return jsonify(latest_emotion)


@app.route("/")
def home():
    return "MoodMate Backend Running"
