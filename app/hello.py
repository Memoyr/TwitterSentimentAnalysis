# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template("home.html")
#
# @app.route("/search",methods=['GET','POST'])
# def search():
#     if request.method == 'POST':
#         search_tweets = request.form['search_tweets']
#         return render_template("sentiment-list.html", search_tweets=search_tweets)
#
#     return render_template("home.html")
#
# @app.route("/sentiment/")
# def list():
#     return render_template("sentiment-list.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)
