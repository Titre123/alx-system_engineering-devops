#!/usr/bin/python3
"""
Query the Reddit API and return the top 10 post for a given subreddit
"""
import requests


def top_ten(subreddit):
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                     format(subreddit),
                     headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if (r):
        children = r.json().get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    else:
        print(None)
