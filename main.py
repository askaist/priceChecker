import requests
from bs4 import BeautifulSoup

URL = "https://www.walmart.com/search?q=milk"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
