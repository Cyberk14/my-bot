from bs4 import BeautifulSoup as BS4
import requests

url = "https://wa.me/256740941194?text=this%20is%20a"
data = requests.get(url).text

soup = BS4(data, "html-parser")

print(soup)