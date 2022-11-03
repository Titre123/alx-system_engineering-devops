#!/usr/bin/python3
"""
Query the Reddit API and return a list containing the titles of all hot
articles for a given subreddit match with word_list
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
  """
  Query the Reddit API and return a list containing the titles of all hot
articles for a given subreddit
  """
  r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after), headers={'User-Agent': 'custom'}, allow_redirects=False)
  if after is None:
    return hot_list
  if (r):
    children = r.json().get('data').get('children')
    for child in children:
      hot_list.append(child.get('data').get('title'))
    recurse(subreddit, hot_list, r.json().get('data').get('after'))
    
    return hot_list
  else:
    return None

def count_words(subreddit, word_list):
  """
  Query the Reddit API and return a list containing the titles of all hot
articles for a given subreddit
  """
  x = []
  y = {}
  list = recurse(subreddit)
  for title in list:
    x += title.split()
  for letter in x:
    for word in (word_list):
      if y.get(word) and word == letter:
        y[word] += 1
      elif word not in y and word == letter:
        y[word] = 1
  for item in sorted(y.keys()):
    print('{}: {}'.format(item, y.get(item)))
