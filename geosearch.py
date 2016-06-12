#-165.41015625,26.8240707805,-63.28125,69.6876184319
import sys
import tweepy


#Variables that contains the user credentials to access Twitter API 

consumer_key="Z3Vic5rs8Qm08xSjJOWZ8JD7W"
consumer_secret="vVLxqPckd8d9tvn8u7Zrwu0mHkHFiAMCYMn1cvWghk8H8YEU63"
access_key="3109190601-KhBFVh3M44FX7ou6q64LogHlMZSu9fWqobgTZ5D"
access_secret="yzlxlKYsiDDMeYbQQkboh70V5g3VCiGVIH6BlLHN3DrJf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'protest' in status.text.lower():
            print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
#sapi.filter(locations=[-6.38,49.87,1.77,55.81])
sapi.filter(locations=[-165.41015625,26.8240707805,-63.28125,69.6876184319])
