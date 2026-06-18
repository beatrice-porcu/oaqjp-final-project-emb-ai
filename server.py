''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000 or other available port.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import custom module
from EmotionDetection.emotion_detection import emotion_detector

# Initiate flask app
app = Flask("Emotion Detector")
''' Define emotiondetection route '''
@app.route("/emotionDetector")
def emotion_detect():
    """Analyze text and return the detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template('index.html')
