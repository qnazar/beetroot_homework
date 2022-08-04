"""Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file"""
import requests
import datetime
import json

url = "https://api.pushshift.io/reddit/comment/search/"
params = {'subreddit': 'owls', 'sort-type': 'created_utc', 'sort': 'asc'}
response = requests.get(url, params)

comments = {}
for num, comment in enumerate(response.json()['data'], start=1):
    body = comment['body']
    time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%Y-%m-%d %H:%M')
    comments[num] = body, time_posted

    print(body)
    print(time_posted)
    print('-------------------------------------')


with open('comments.json', 'w') as file:
    json.dump(comments, file, indent=4)
