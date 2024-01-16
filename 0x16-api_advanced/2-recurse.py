#!/usr/bin/python3
"""
recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if not after:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{\
                subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)

        if children:
            for post in children:
                title = post.get('data', {}).get('title', '')
                hot_list.append(title)

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
