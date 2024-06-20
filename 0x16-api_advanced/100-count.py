#!/usr/bin/python3
"""queries the reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords"""

import requests


def count_words(subreddit, word_list=[], word_dict={}, after=None):
    """queries the reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords"""
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
            words = post['data']['title'].lower().split()
            for word in words:
                if word in word_list:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        if after is not None:
            count_words(subreddit, word_list, word_dict, after)
        return word_dict
    return None