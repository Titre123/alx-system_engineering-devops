#!/usr/bin/python3
""" Query the Reddit API and return the numbe
r of subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ return no of suscribers """
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if (r):
        return r.json().get('data').get('subscribers')
    else:
        return 0
