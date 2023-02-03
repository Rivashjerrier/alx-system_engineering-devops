#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def title(list, articles):
    """ Store articles in a list """
    if len(articles) == 0:
        return
    list.append(articles[0]['data']['title'])
    articles.pop(0)
    title(list, articles)


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
    if res.status_code != 200:
        return None
    dict = res.json()
    articles = dict['data']['children']
    title(list, articles)
    after = dict['data']['after']
    if not after:
        return list
    return recurse(subreddit, list=list, after=after)
