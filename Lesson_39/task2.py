"""Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API."""
import requests
import datetime
import json
from concurrent.futures import ProcessPoolExecutor


params = [{'subreddit': 'ladygaga', 'sort-type': 'created_utc', 'sort': 'asc'},
          {'subreddit': 'britney', 'sort-type': 'created_utc', 'sort': 'asc'},
          {'subreddit': 'beyonce', 'sort-type': 'created_utc', 'sort': 'asc'}]


def download_comments(params):
    url = "https://api.pushshift.io/reddit/comment/search/"
    response = requests.get(url, params)
    if response.status_code == 200:
        comments = {}
        for num, comment in enumerate(response.json()['data'], start=1):
            body = comment['body']
            time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%Y-%m-%d %H:%M')
            comments[num] = body, time_posted
        with open(f'{str(params["subreddit"])}-comments.json', 'w') as file:
            json.dump(comments, file, indent=4)
    elif response.status_code == 404:
        print("No such page", str(params["subreddit"]))


if __name__ == '__main__':
    with ProcessPoolExecutor(len(params)) as executor:
        executor.map(download_comments, params)