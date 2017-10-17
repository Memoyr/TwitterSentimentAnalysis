import tweepy
from textblob import TextBlob
import decimal


# Step 1 - tweeter app config
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
search_tweet = input("Enter a subject to search on Twitter: ")
public_tweets = api.search(search_tweet)

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
    neutral_total = str(average_polarity_in_percent(percentage_of_list(polarity_list.count(0.0), polarity_list))) + "% of collected data are Neutral"
    positive_total = str(average_polarity_in_percent(percentage_of_list(qty_positive, polarity_list))) + "% of collected data are Positive "
    negative_total = str(average_polarity_in_percent(percentage_of_list(qty_negative, polarity_list))) + "% of collected data are Negative "

    return str(positive_total+"\n"+neutral_total+"\n"+negative_total+"\n")

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

average_list=[]

with open("result.txt",'w+') as file:
    for tweet in public_tweets:
        #print(tweet.text)

        #Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        #print("")
        file.write(str(analysis.polarity)+"\n")
        average_list.append(analysis.polarity)



print("\nHERE IS YOUR ANALYSIS: \n")
print("The average feeling is " + generate_polarity_label(average_list).upper())
print(str(percentage_against_polarity_type(average_list)))
print("Calculation based on " + str(len(public_tweets)) +  " tweet collected \n")
