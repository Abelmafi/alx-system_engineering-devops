#!/usr/bin/python3
"""Api request to reddit about sub reddit subscribe count"""
import requests


def number_of_subscribers(subreddit):
    """..."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent": "MyAPI/0.01"}
    res = requests.get('https://www.reddit.com/r/' + subreddit +
                       '/about.json', headers=headers)
    if res.status_code != 200:
        return 0
    return res.json()['data']['subscribers']
