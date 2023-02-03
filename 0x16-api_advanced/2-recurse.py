#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def article_title(hot_list, hot_articles):
    """ Store articles in a list """
    if len(hot_articles) == 0:
        return
    hot_list.append(hot_articles[0]['data']['title'])
    hot_articles.pop(0)
    article_title(hot_list, hot_articles)


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

    dic = res.json()
    hot_articles = dic['data']['children']
    article_title(hot_list, hot_articles)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
