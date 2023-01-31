#!/usr/bin/python3
"""Api request to reddit about sub reddit subscribe count"""
import requests


def top_ten(subreddit):
    """..."""
    headers = {"User-Agent": "MyAPI/0.0.2"}
    res = requests.get('https://www.reddit.com/r/' + subreddit +
                       '/hot.json?limit=10', headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return ("None")
    for i in range(10):
        print(res.json()['data']['children'][i]['data']['title'])
