#!/usr/bin/python3
"""
queries the Reddit API & returns->numb of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """return the total number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/meron_student)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if subreddit is None or type(subreddit) is not str:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
