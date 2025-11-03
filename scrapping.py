import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r =requests.get(url)
soup = BeautifulSoup(r.text , "lxml")

tag = soup.find_all("a" , class_ = "title")

product = []

for i in tag:
    name = i.text.strip()
    product.append(name)
    
print(product)    