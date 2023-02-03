#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", num=0):
    """ Queries Reddit API returns a list containing the title """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    params = {
       'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if response.status_code == 404:
        return None

    dic = response.json().get('data')
    after = dic.get('after')
    num += dic.get('dist')
    for n in dic.get('children'):
        hot_list.append(n.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, num)
    return hot_list
