#!/usr/bin/python3
"""returns a list containing the tiltles of all hot articles
recursivly"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the tiltles of all hot articles
    recursivly"""
    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(subreddit,
                                                                  after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        for post in data['data']['children']:
            title = post['data']['title']
            hot_list.append(title)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None