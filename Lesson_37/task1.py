"""Download and save to file robots.txt from wikipedia, twitter websites etc."""
import requests

url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url)
with open('Robots_wiki.txt', 'w') as file:
    file.write(response.text)

url = "https://twitter.com/robots.txt"
response = requests.get(url)
with open('Robots_twitter.txt', 'w') as file:
    file.write(response.text)


