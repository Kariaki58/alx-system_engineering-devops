#!/usr/bin/python3
"""check how many subsribers"""
import requests

headers = {'User-Agent': 'MyCustomUserAgent/1.0'}


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
