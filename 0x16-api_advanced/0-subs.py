#!/usr/bin/python3
"""check how many subsribers"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyBot/1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"Error: {response.status_code}")
    return 0
