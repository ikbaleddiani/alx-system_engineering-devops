#!/usr/bin/python3
"""return the top ten hot posts titles"""

import requests


def top_ten(subreddit):
    """return the top ten hot posts titles"""
    headers = {
             'User-Agent': 'Your-User-Agent-Name'
             }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            title = post['data']['title']
            print(title)
    print(None)