#!/usr/bin/python3
"""
- Recursive function that queries the Reddit API
- and returns a list containing the titles of all hot articles
- for a given subreddit. If no results are found for the given subreddit,
- the function should return None.

- Hint: The Reddit API uses pagination for separating pages of responses.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    - Recursive function that queries the Reddit API
    - and returns a list containing the titles of all hot articles
    - for a given subreddit. If no results are found for the given subreddit,
    - the function should return None.

    - Hint: The Reddit API uses pagination for separating pages of responses.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Reddit_title_of_all_hot_articles_script"
    }

    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            posts = data['data']['children']

            # Add the titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there's more data to fetch (pagination)
            after = data["data"].get("after")

            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
        else:
            # If status code indicates an error, return None
            return None
    except Exception:
        return None
