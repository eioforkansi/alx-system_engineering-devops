#!/usr/bin/python3
"""
- Function that queries the Reddit API
- and prints the titles of the first 10 hot posts
- listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    - Function that queries the Reddit API
    - and prints the titles of the first 10 hot posts listed
    - for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Reddit_10_hot_post_script"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except Exception:
        print("None")
