import tweepy
import time
from pprint import pprint
import requests
import re

with open("api_keys.txt") as file:
    key_list = file.readlines()

consumer_key = key_list[0].strip("\n")
consumer_secret = key_list[1].strip('\n')
access_token = key_list[2].strip('\n')
access_token_secret = key_list[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
text_query = '#Blueprint2020'
count = 70
try:
    # Pulling individual tweets from query
    for tweet in api.search(q=text_query, count=count):
        # Adding to list that contains all tweets
        tweets.append((tweet.created_at, tweet.id, tweet.text))
except BaseException as e:
    print('failed on_status,', str(e))
    time.sleep(3)

pprint(tweets)
valid_links = []
with open("valid_links.txt", "r") as tweet_file:
    for item in tweet_file.readlines():
        valid_links.append(item.replace("\n", ""))
print(valid_links)
for tweet in range(len(tweets)):
    result = tweets[tweet][2][-23:]

    result = str(requests.get(result).content)

    with open("regex.txt", "r") as reg:
        regex = reg.read()

    q = re.search(regex, result)

    q = str(q)[-49:-2]
    if q[-3:] == "jpg" and tweet not in valid_links:
        valid_links.append(q)

    print(q)


valid_links = set(valid_links)

with open("valid_links.txt", "w") as tweet_file:
    for item in valid_links:
        tweet_file.write(f"{item}\n")
