#!/usr/bin/python3
"""returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    params = {
            "limit": 100,
            "after": after
            }
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False).json()
    children = response.get("data", {}).get("children", None)
    pagination = response.get("data", {}).get("after", None)

    if pagination is not None:
        if children:
            for item in children:
                hot_list.append(item.get("data").get("title"))

        if pagination is not None:
            recurse(subreddit, hot_list, pagination)
        return hot_list
    else:
        return None
