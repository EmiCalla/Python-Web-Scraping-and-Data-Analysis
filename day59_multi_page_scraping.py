# Day 59(05-09-2026):

import requests
from bs4 import BeautifulSoup
import pandas as pd

homepage = 'http://books.toscrape.com/'

page_urls = []
dic_list = []

for page in range(1,6):
    numbered_page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'

    if page == 1:
        url = homepage
    else:
        url = numbered_page_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    page_urls.append(url)

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
        

    print("\n" + "   " + "=" * 50 + "\n")

with open('page_url.txt', 'w') as pages:
    pages.write("\n".join(page_urls))


df = pd.DataFrame(dic_list)
df['Price'] = df['Price'].str.replace('Â£', '')
df['Price'] = df['Price'].astype(float)
df.to_csv('books.csv', index=False)

print(len(dic_list))
print(df.head())
print()
print(df.tail())
print("\n" + "   " + "=" * 50 + "\n")
