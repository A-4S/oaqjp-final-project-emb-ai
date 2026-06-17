from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion():
    req = request.args.get("textToAnalyze")

    e = emotion_detector(req)

    if e["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {e['anger']}, 'disgust': {e['disgust']}, 'fear': {e['fear']}, 'joy': {e['joy']}, and 'sadness': {e['sadness']}. The dominant emotion is {e['dominant_emotion']}."


@app.route("/")
def index_route():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
