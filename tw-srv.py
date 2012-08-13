from os import environ

from flask import Flask, jsonify
import tweepy

app = Flask(__name__)

# Account User Names
TWITTER_NAME = 'tobywaite'
YELP_NAME = 'ybot_yelp' # Name of the twitter acct aggragating yelp checkins

# Twitter auth info & setup
T_CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
T_CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
T_ACCESS_TOKEN = environ['TWITTER_ACCESS_TOKEN']
T_ACCESS_SECRET = environ['TWITTER_ACCESS_SECRET']

twitter_auth = tweepy.OAuthHandler(T_CONSUMER_KEY, T_CONSUMER_SECRET)
twitter_auth.set_access_token(T_ACCESS_TOKEN, T_ACCESS_SECRET)

twitterAPI = tweepy.API(twitter_auth)


@app.route('/blog')
def blog():
    """Returns the first several blog/project posts"""
    return jsonify(
        [
            {
                'title': 'A blog post about things',
                'date': '7/3/12',
                'id': 1,
                'lead': "once upon a time, there was a cool dude who did cool \
                things. This is his story.",
                'body': "More content for the blog post",
                'more_url': 'http://blog.tobywaite.net',
            },
            {
                'title': 'Cool projects, ftw',
                'date': '6/3/12',
                'id': 2,
                'lead': "I did a really cool project once, this is all about \
                it.",
                'body': "More content for the blog post",
                'more_url': 'http://blog.tobywaite.net',
            },
        ]
    )

@app.route('/twitter')
@app.route('/twitter/<n>')
def twitter(n=1):
    """Returns a tweet from my timeline"""
    tweet = get_tweet(TWITTER_NAME, n)
    tweet_info = {
           'text': tweet.text,
           'date': tweet.created_at.strftime('%A, %B %d'),
           'time': tweet.created_at.strftime('%H:%M'),
           'latest': (int(n) == 1), # True if n is one, else False.
        }
    return jsonify(tweet_info)

@app.route('/yelp')
@app.route('/yelp/<n>')
def yelp(n=1):
    """Return yelp activity from my checkin stream"""
    tweet = get_tweet(YELP_NAME, n) # Yelp checkin info is aggregated to twitter.
    yelp_info = {
        'biz-name': parse_yelp_name(tweet.text),
        'biz-uri': parse_yelp_uri(tweet.text),
        'location': 'San Francisco, CA',
        'date': tweet.created_at.strftime('%A, %B %d'),
        'time': tweet.created_at.strftime('%H:%M'),
        'tip': "",
    }
    return jsonify(yelp_info)

def parse_yelp_name(text):
    """Tweets are in the following form:
        'I checked in at Tilden Regional Park on #Yelp http://bit.ly/td3IN5'
    This function pulls the "Tilden Regional Park" out of the text.
    """
    end_index = text.find('on #Yelp')
    start_index = len('I check in at ')
    return text[start_index:end_index]

def parse_yelp_uri(text):
    """Tweets are in the following form:
        'I checked in at Tilden Regional Park on #Yelp http://bit.ly/td3IN5'
    This function pulls the "http://bit.ly/td3IN5" out of the text.
    """
    start_index = text.find('http://bit.ly/')
    return text[start_index:]

def parse_biz_uri(text):
    pass

def get_tweet(username, n):
    """Returns the n'th tweet from a users twitter timeline

    This is an ugly hack. The twitter API doesn't allow you to naievly get
    the "nth" tweet. Instead, we get the first "n" tweets and return the last
    one returned.

    Args:
    - username: the username of the account to fetch the tweet for.
    - n: the number of the tweet to get on their time line. n=1 indicates the
       most recent tweet, n=10 indicates the 10th most recent, etc.

    Returns:
    - A tweepy Status object
    """
    return twitterAPI.home_timeline(count=n)[-1:][0] # Just the specified tweet.

if __name__ == '__main__':
    app.run()
