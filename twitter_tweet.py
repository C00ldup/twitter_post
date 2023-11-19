import dogs_facts
import twitter_token
from creds import api_key, api_secret, access_token, access_token_secret

def post_tweet(api, text):
    api.create_tweet(text=text)

api = twitter_token.get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret)
text = dogs_facts.get_fact()
post_tweet(api, text)