from flask import render_template, request, redirect
from app import app
from .tweetSearch import Search


@app.route('/',methods=['GET','POST'])
#@app.route('/index',methods=['GET','POST'])
def index():
    search = Search()
    if request.method == 'POST':
        search_tweets = request.form['search_tweets']
        search.authenticate(search_tweets)
        list = search.average_list
        generate_polarity_label = search.generate_polarity_label
        percentage_neutral      = search.neutral_total
        percentage_positive     = search.positive_total
        percentage_negative     = search.negative_total
        public_tweets           = search.public_tweets
        return render_template("sentiment-list.html",
                                search_tweets=search_tweets,
                                average_list=list,
                                generate_polarity_label=generate_polarity_label,
                                percentage_neutral=percentage_neutral,
                                percentage_positive=percentage_positive,
                                percentage_negative=percentage_negative,
                                public_tweets=public_tweets)

    return render_template("home.html")

@app.route("/sentiment/")
def list():
    return render_template("sentiment-list.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)
