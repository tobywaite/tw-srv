from flask import Flask, jsonify
from os import environ

app = Flask(__name__)

# Blog

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

# Twitter

import tweepy

t_consumer_key = environ['TWITTER_CONSUMER_KEY']
t_consumer_secret = environ['TWITTER_CONSUMER_SECRET']
t_access_token = environ['TWITTER_ACCESS_TOKEN']
t_access_secret = environ['TWITTER_ACCESS_SECRET']

twitter_auth = tweepy.OAuthHandler(t_consumer_key, t_consumer_secret)
twitter_auth.set_access_token(t_access_token, t_access_secret)

twitter = tweepy.API(twitter_auth)

@app.route('/tweets/<username>')
def tweets(username):
    """Returns the most recent tweet from a twitter user's timeline"""
    return get_tweets(username, n=1)

@app.route('/tweets/<username>/<n>')
def get_tweets(username, n):
    """Returns the n'th tweet from a users twitter timeline"""
    return twitter.home_timeline(count=1)
    #return jsonify(
    #    {
    #        'tweet': 'This is my tweet!',
            #'date': '6/15/12',
        #}
    #)

# Github

@app.route('/github/<username>/')
def github(username):
    """Returns the most recent commit from a user"""
    return github_activity(username, activity_type='commit', n=1)

@app.route('/github/<username>/<activity>/<n>')
def github_activity(username, activity):
    """Returns the n'th most recent of a given activity for a given user's
    github account
    """
    return jsonify({'commit': 'my commit messages are so dumb'})

# Last.fm

@app.route('/lastfm/<username>')
def lastfm(username):
    """Return the most recent track played by a given last.fm user"""
    return lastfm_activity(username, n=1)

@app.route('/lastfm/<username>/<n>')
def lastfm_activity(username, n):
    """Return the n'th most recent track played by a given last.fm user"""
    return jsonify(
        {
            'artist': 'Beach House',
            'album': 'Bloom',
            'song': 'A song',
            'album_art': 'http://www.google.com',
        }
    )

# Flickr

@app.route('/flickr/<username>')
def flickr(username):
    """Return the most recent track played by a given last.fm user"""
    return lastfm_activity(username, n=1)

@app.route('/lastfm/<username>/<album>/<n>')
def flickr_photo(username, album, n):
    """Return the n'th photo from a specified album belonging to a flickr user"""
    return jsonify(
        {
            'title': 'A picture',
            'url': 'http://www.flickr.com',
            'size': {'width': 300, 'height': 200},
            'desc': 'This is a picture of a thing',
        }
    )

# Yelp

@app.route('/yelp/<username>')
def yelp(username):
    return yelp_checkin(username, n=1)

@app.route('/yelp/<username>/<n>')
def yelp_checkin(username, n):
    return jsonify(
        {
            'location': "Ike's Place",
            'date': '12/3/12',
            'tip': 'This place makes sandwiches.',
        }
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
