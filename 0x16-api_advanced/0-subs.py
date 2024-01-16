#!/usr/bin/python3
"""check how many subsribers"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    return 0
