"""Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump them to a file.
For this task use asyncio and aiohttp libraries for making requests to Reddit API."""
import asyncio
import aiohttp
import time
import json

url = 'https://api.pushshift.io/reddit/comment/search/'
params = [{'subreddit': 'ladygaga', 'sort-type': 'created_utc', 'sort': 'asc'},
          {'subreddit': 'britney', 'sort-type': 'created_utc', 'sort': 'asc'},
          {'subreddit': 'beyonce', 'sort-type': 'created_utc', 'sort': 'asc'}]


async def get_comments(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response = await response.json()
            with open(f'comments-{params["subreddit"]}.json', 'w') as file:
                json.dump(response, file, indent=4)


async def main():
    tasks = []
    for par in params:
        tasks.append(asyncio.create_task(get_comments(url, par)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
