#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except KeyError:
        return 0