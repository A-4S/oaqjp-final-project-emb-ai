"""
This module consists of the server routes for the Emotion Detection app.

Attributes:
    app (Flask): The Flask server application.

Functions:
    emotion():
        Returns result of emotion detection.
    
    index():
        Returns a render of the index page.
"""


from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion():
    """emotionDetector route.
    
    Returns:
        str: result of emotion detection.
    
    """

    req = request.args.get("textToAnalyze")

    e = emotion_detector(req)

    if e["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is \
        'anger': {e['anger']}, 'disgust': {e['disgust']}, \
        'fear': {e['fear']}, 'joy': {e['joy']}, and 'sadness': {e['sadness']}. \
        The dominant emotion is {e['dominant_emotion']}."


@app.route("/")
def index():
    """emotionDetector route.
    
    Returns:
        any: render of the index page.
    
    """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
