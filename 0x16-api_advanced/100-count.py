#!/usr/bin/python3
"""
- Recursive function that queries the Reddit API,
- parses the title of all hot articles,
- and prints a sorted count of given keywords
- (case-insensitive, delimited by spaces.
- Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, after='', word_count=None):
    """
    - Recursive function that queries the Reddit API,
    - parses the title of all hot articles,
    - and prints a sorted count of given keywords
    - (case-insensitive, delimited by spaces.
    - Javascript should count as javascript, but java should not).
    """

    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return
    except Exception:
        return

    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')



    for post in posts:
        title = post['data']['title'].lower().split()
        for word in word_list:
            lower_word = word.lower()
            word_count[lower_word] = word_count.get(lower_word, 0) + title.count(lower_word)

    if after:
        count_words(subreddit, word_list, after, word_count)

    if after is None:
        sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f'{word}: {count}')
