#!/usr/bin/python3
"""
- Function that queries the Reddit API
- and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    - Function that queries the Reddit API and
    - returns the number of subscribers (not active users, total subscribers)
    - for a given subreddit.
    - If an invalid subreddit is given,
    - the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Reddit_subscriber_script"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
