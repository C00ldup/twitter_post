import twitter_token
from creds import api_key, api_secret, access_token, access_token_secret

client_v1 = twitter_token.get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret)
client_v2 = twitter_token.get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret)

media_path = "path_to_media"
media = client_v1.media_upload(filename=media_path)
media_id = media.media_id

client_v2.create_tweet(text="Tweet text", media_ids=[media_id])