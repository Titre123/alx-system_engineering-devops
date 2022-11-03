#!/usr/bin/python3
"""
Query the Reddit API and return a lit containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Reddit API and return a lit containing the titles of all hot articles
    """
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, after),
                     headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if after is None:
        return hot_list
    if (r):
        children = r.json().get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        recurse(subreddit, hot_list, r.json().get('data').get('after'))
        return hot_list
    else:
        print(None)
