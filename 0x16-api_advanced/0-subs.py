#!/usr/bin/python3
"""Queries Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a given subreddit"""
    url = "http://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    dic = response.json()
    if "data" not in dic:
        return 0
    if "subscribers"not in dic.get("data"):
        return 0
    return response.json()["data"]["subscribers"]
