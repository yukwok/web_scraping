import requests
from bs4 import BeautifulSoup as BS

response = requests.get(url="https://news.ycombinator.com/news")


soup = BS(markup=response.text, features="html.parser")
# class is python key word
storylinks = soup.find_all(name="a", class_="storylink")


print(storylinks[0].get("href"))
