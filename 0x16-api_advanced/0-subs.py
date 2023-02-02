#!/usr/bin/python3
"""0-subs - Queries the Reddit API and returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers for a given subreddit
    """
    api = "http://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(api, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    subscribers = response.json().get("data")
    return subscribers.get("subscribers")
