import random

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

    return jsonify({"status": "received"})

