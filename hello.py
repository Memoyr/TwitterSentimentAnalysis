from flask import Flask
app = Flask(__name__)

keywordSentiment="test"
@app.route("/")
def hello():
    return "<i>Hello World!</i><input>" + keywordSentiment + "</input>"

def yourSentiment(sentiment):
    print("OK lets search for :" + keywordSentiment)
