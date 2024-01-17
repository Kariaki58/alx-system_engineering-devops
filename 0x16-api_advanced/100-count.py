#!/usr/bin/python3
"""
count it
"""
import json
import urllib.request


def fetch_json(url):
    """fetch json"""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

def count_words(subreddit, word_list, after=None, counts=None):
    """count words"""
    if counts is None:
        counts = {}

    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        url = base_url if after is None else f'{base_url}?after={after}'
        data = fetch_json(url)
        for post in data['data']['children']:
            count_words(subreddit, word_list, after=post['data']['name'], counts=counts)
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error fetching data from Reddit: {e}")
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
