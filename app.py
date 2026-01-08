from flask import Flask, request, jsonify

app = Flask(__name__)
latest_emotion = "neutral"

@app.route("/emotion", methods=["POST"])
def receive_emotion():
    global latest_emotion
    data = request.json
    latest_emotion = data["emotion"]
    return jsonify({"status": "received"})

@app.route("/emotion", methods=["GET"])
def send_emotion():
    return jsonify({"emotion": latest_emotion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
