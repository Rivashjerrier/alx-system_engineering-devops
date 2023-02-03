#!/usr/bin/python3
"""Recursive function queries Reddit API and returns list containing titles"""
import requests
import sys


def recurse(subreddit, hot_list=[], after="", num=0):
    """Queries the Reddit API and returns a list containing the title."""
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    params = {
       'after': after,
       'num': num,
       'limit': 100
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if response.status_code == 404:
        return None
    dic = response.json().get("data")
    after = dic.get("after")
    num += dic.get("dist")
    for n in dic.get("children"):
        hot_list.append(n.get("data").get("title"))
    if after is not None
        return recurse(subreddit, hot_list, after, num)
    return hot_list
