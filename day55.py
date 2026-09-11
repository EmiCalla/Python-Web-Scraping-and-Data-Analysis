# Day 55(01-09-2026):

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

dic_list = []

for book in books:
    title = book.div.a.img['alt']
    product_price = book.find('div', class_='product_price')
    product_rating = book.find('p', class_='star-rating')
    availability_check = book.find('p', class_='instock availability')
    availability = availability_check.text.strip()
    link = book.h3.a['href']
    price = product_price.p.text
    rating = product_rating['class'][1]

    print("\n" + "   " + "=" * 50 + "\n")
    print(f'Title : {title}')
    print(f'Price : {price}')
    print(f'Rating : {rating}')
    print(f'Availability : {availability}')
    print(f'Book_Link : {link}')

    dic_list.append({'Title' : title,
           'Price' : price,
           'Rating' : rating,
           'Availability' : availability,
           'Link': link})

df = pd.DataFrame(dic_list)

df['Price'] = df['Price'].str.replace('Â£', '')
df['Price'] = df['Price'].astype(float)
print(df['Price'].dtype)

df.to_csv('books.csv', index=False)