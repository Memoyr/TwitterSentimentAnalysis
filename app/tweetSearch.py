import tweepy
from flask import Flask, render_template, request
from textblob import TextBlob
import decimal

class Search():

    generate_polarity_label = ""
    def authenticate(self,search_tweet):
        average_list=[]
        # Step 1 - tweeter app config
        consumer_key= ''
        consumer_secret= ''

        access_token=''
        access_token_secret=''

        # Authenticate tweeter app
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        #places = api.geo_search(query="USA", granularity="country")
        #place_id = places[0].id
        # Retrieve Tweets
        public_tweets = api.search(q=search_tweet,count=100) # geocode="37.781157, -122.398720, 1mi",

        with open("result.txt",'w+') as file:
            for tweet in public_tweets:
                #print(tweet.text)

                # Perform Sentiment Analysis on Tweets
                analysis = TextBlob(tweet.text)
                # Write result in file
                file.write(str(analysis.polarity)+"\n")
                # Create a list with all polarity collected
                average_list.append(analysis.polarity)
        self.average_list = average_list
        self.public_tweets = len(public_tweets)

        def average_polarity_in_percent(average_val):
            a = decimal.Decimal(average_val)
            av = round(a,2)
            return abs(av*100)

        def percentage_of_list(x,list):
            percentage = x/len(list)
            return percentage

        def percentage_against_polarity_type(polarity_list):
            qty_positive=0
            qty_negative=0
            for item , val in enumerate(polarity_list):
                if (val > 0) and (val != 0):
                    qty_positive +=1
                if (val < 0) and (val != 0):
                    qty_negative +=1
            self.neutral_total = float(average_polarity_in_percent(percentage_of_list(polarity_list.count(0.0), polarity_list))) # + "% of collected data are Neutral"
            self.positive_total = float(average_polarity_in_percent(percentage_of_list(qty_positive, polarity_list))) # + "% of collected data are Positive "
            self.negative_total = float(average_polarity_in_percent(percentage_of_list(qty_negative, polarity_list))) # + "% of collected data are Negative "
            #return positive_total , neutral_total , negative_total

        def average_polarity(pol):
            for item , val in enumerate(pol):
                val +=val
                if item == len(pol): # if my loop is completed
                    val= val/len(pol)
            return int(average_polarity_in_percent(val))


        # write average polarity with label
        # get average_polarity label
        def generate_polarity_label(float_pol):
            label = "neutral"
            if average_polarity(float_pol) != 0.0:
                if average_polarity(float_pol) > 0:
                    label = "positive"
                else:
                    label = "negative"
            return label

        self.generate_polarity_label = generate_polarity_label(average_list).upper()
        self.percentage_against_polarity_type = str(percentage_against_polarity_type(self.average_list))
