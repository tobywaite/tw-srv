from flask import Flask, jsonify
app = Flask(__name__)

# Blog

@app_route('/blog')
def blog():
    """Returns the first several blog/project posts"""
    return jsonify(
        [
            {
                'title': 'A blog post about things',
                'date': '7/3/12',
                'id': 1,
                'lead': "once upon a time, there was a cool dude who did cool
                things. This is his story."
                'body': "More content for the blog post",
                'more_url': 'http://blog.tobywaite.net',
            },
            {
                'title': 'Cool projects, ftw',
                'date': '6/3/12',
                'id': 2,
                'lead': "I did a really cool project once, this is all about it."
                'body': "More content for the blog post",
                'more_url': 'http://blog.tobywaite.net',
            },
        ]

# Twitter

@app_route('/tweets/<username>')
def tweets(username):
    """Returns the most recent tweet from a twitter user's timeline"""
    return get_tweets(username, n=1)

@app_route('/tweets/<username>/<n>')
def get_tweets(username, n):
    """Returns the n'th tweet from a users twitter timeline"""
    return jsonify(
        {
            'tweet': 'This is my tweet!',
            'date': '6/15/12',
        }
    )

# Github

@app_route('/github/<username>/')
def github(username):
    """Returns the most recent commit from a user"""
    return github_activity(username, activity_type='commit', n=1)

@app_route('/github/<username>/<activity>/<n>')
def github_activity(username, activity):
    """Returns the n'th most recent of a given activity for a given user's
    github account
    """
    return jsonify({'commit': 'my commit messages are so dumb'})

# Last.fm

@app_route('/lastfm/<username>')
def lastfm(username):
    """Return the most recent track played by a given last.fm user"""
    return lastfm_activity(username, n=1)

@app_route('/lastfm/<username>/<n>')
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

@app_route('/flickr/<username>')
def flickr(username):
    """Return the most recent track played by a given last.fm user"""
    return lastfm_activity(username, n=1)

@app_route('/lastfm/<username>/<album>/<n>')
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

@app_route('/yelp/<username>')
def yelp(username):
    return yelp_checkin(username, n=1)

@app_route('/yelp/<username>/<n>')
def yelp_checkin(username, n)
    return jsonify(
        {
            'location': "Ike's Place"
            'date': '12/3/12',
            'tip': 'This place makes sandwiches.',
        }
    )

