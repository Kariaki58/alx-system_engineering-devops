#!/usr/bin/python3
"""
count it
"""
import requests


def count_words(subreddit, word_list, after="", counts=0):
    """count words"""
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": counts,
        "limit": 100
    }
    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = results.get("data")
    new_after = data.get("after")
    new_total_count = counts + data.get("dist")

    word_instances = {}
    for child in data.get("children"):
        title_words = child.get("data").get("title").lower().split()
        for search_word in word_list:
            if search_word.lower() in title_words:
                occurrences = title_words.count(search_word.lower())
                if word_instances.get(search_word) is None:
                    word_instances[search_word] = occurrences
                else:
                    word_instances[search_word] += occurrences

    if new_after is None:
        if not word_instances:
            print("")
            return
        sorted_word_instances = sorted(
                word_instances.items(), key=lambda kv: (-kv[1], kv[0])
                )
        for word, count in sorted_word_instances:
            print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, new_after, new_total_count)
