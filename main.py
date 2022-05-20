import os
from dotenv import load_dotenv
import tweepy
import pandas as pd

load_dotenv('.env')
BEARER = os.environ.get('BEARER')
print(BEARER)
query = "twitter"
limit = 500

client = tweepy.Client(BEARER)

df_tweets = pd.DataFrame()
tweets = tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=['created_at', 'author_id', 'public_metrics', 'lang'],
    max_results=100
).flatten(limit=limit)
for tweet in tweets:
    df_tweets = pd.concat([df_tweets, pd.DataFrame([tweet.data])], ignore_index=True)

print(df_tweets)