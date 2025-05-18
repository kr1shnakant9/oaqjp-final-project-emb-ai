from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emo():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: Please provide 'textToAnalyze' query parameter.", 400

    re = emotion_detector(text_to_analyze)
    dominant_emotion = re['dominant_emotion']

    ansre = f"For the given statement, the system response is: {re}\nThe dominant emotion is: {dominant_emotion}"
    return ansre

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
