#!/usr/bin/python3
"""Queries Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a given subreddit"""
    url = "http://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if subreddit is None or type(subreddit) is not str:
        return 0
    subs = response.get("data", {}).get("subscribers", 0)
    return subs
