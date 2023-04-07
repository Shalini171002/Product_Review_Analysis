from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_review():
    review = request.form['review']
    blob = TextBlob(review)
    score = round((blob.sentiment.polarity + 1) * 2.5, 1)
    return render_template('predict.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
