
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return jsonify({"error": "Please provide text to analyze."}), 400

    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
