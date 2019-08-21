import requests
from bs4 import BeautifulSoup

r = requests.get("https://gamewith.jp/pricone-re/")

soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("ul", "newsFeed_list").text)
