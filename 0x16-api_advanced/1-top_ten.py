#!/usr/bin/python3
"""Api request to reddit about sub reddit subscribe count"""
import requests


def top_ten(subreddit):
    """..."""
    headers = {"User-Agent": "MyAPI/0.0.2"}
    params = {
            "limit": 10
            }
    res = requests.get('https://www.reddit.com/r/' + subreddit +
                       '/hot.json?limit=10', params=params, headers=headers,
                       allow_redirects=False)

    if res.status_code != 200:
        print("None")
        return

    for i in res.json()['data']['children']:
        print(i['data']['title'])
