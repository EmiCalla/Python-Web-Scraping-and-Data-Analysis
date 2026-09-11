# Day 50,51,52,53(27-08-2026):
# Web scrapping

import requests 
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all('article', class_="product_pod")
products_price = soup.find_all('div', class_="product_price")
book_rating = soup.find("p", class_ = "star-rating Three")
rating = book_rating.text

print("\n" + "   " + "=" * 50 + "\n")

for book in books:
    title = book.div.a.img['alt']
    price_container = book.find('div', class_="product_price")
    rating_tag = book.find('p', class_='star-rating')
    rating = rating_tag['class'][1]
    price = price_container.p.text
    print(f'Title : {title} , Price :  {price}, Rating :{rating}')

print("\n" + "   " + "=" * 50 + "\n")
