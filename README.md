# TwitterSentimentAnalysis
I'm learning python for data science here I'm using Textblob and Tweepy to generate a Twitter Sentiment Analysis.
(Based on this tutorial https://youtu.be/o_OZdbCzHUA)

- I've added extra challenge :

- UI Implementation with Flask.

User search for keywords on Twitter and will receive :

- the average feeling polarity as a label (Positive, Neutral, Negative)
- % of each label Types

- It also create a new textfile with a list of all polarity collected.

## Install
Make a new virtualenv: ```virtualenv env```

Activate the virtualenv: ```source env/bin/activate```

Install Flask: ```pip3 install Flask```

Install Tweepy: ```pip3 install Tweepy```

Install Texblob: ```pip3 install textblob```

Run the project : ```python3 run.py```
