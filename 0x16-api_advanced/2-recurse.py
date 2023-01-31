#!/usr/bin/python3
"""Api request to reddit about sub reddit subscribe count"""
import requests


def recurse(subreddit, after='', hot_list=[]):
    """..."""
    if subreddit is None or type(subreddit) is not str:
        return None
    headers = {"User-Agent": "MyAPI/0.0.2"}
    params = {
            "after": after,
            'limit': 100
            }
    res = requests.get('https://www.reddit.com/r/' + subreddit +
                       '/hot.json', params=params, headers=headers,
                       allow_redirects=False)

    if res.status_code == 404:
        return None

    for data in res.json()['data']['children']:
        hot_list.append(data.get('data').get('title'))

    after = res.json()['data']['after']
    if params['after'] is not None:
        return recurse(subreddit, after, hot_list)

    return hot_list
