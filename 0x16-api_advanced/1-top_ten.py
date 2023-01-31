#!/usr/bin/python3
"""Api request to reddit about sub reddit subscribe count"""
import requests


def top_ten(subreddit):
    """..."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent": "MyAPI/0.0.2"}
    res = requests.get('https://www.reddit.com/r/' + subreddit +
                       '/hot.json', headers=headers)

    if res,status_code != 200:
        return 0
    for i in range(10):
        print(res.json()['data']['children'][i]['data']['title'])
