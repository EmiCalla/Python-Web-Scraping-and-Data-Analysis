# Day 64,65(10,11-09-2026):

import requests 
from bs4 import BeautifulSoup

def scrap_func(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
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
            dic_list.append({'Title' : title,
            'Price' : price,
            'Rating' : rating,
            'Availability' : availability,
            'Link': link})
    return dic_list

all_books = []

homepage = 'http://books.toscrape.com/'

for page in range(1,6):
    numbered_page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'

    if page == 1:
        url = homepage
    else:
        url = numbered_page_url
    opened = False
    for attempt in range(3):
        try:
            result = scrap_func(url)
            opened = True
            break
        except requests.exceptions.Timeout:
            print('Taking too much time. Request failed.')
        except requests.exceptions.RequestException:
            print(f'Page {page} failed!')
    if opened == False:
        continue
    all_books.extend(result)
    for book in result:
        print("\n" + "   " + "=" * 50 + "\n")
        print(f"Title : {book['Title']}")
        print(f"Price : {book['Price']}")
        print(f"Rating : {book['Rating']}")
        print(f"Availability : {book['Availability']}")
        print(f"Book_Link : {book['Link']}")
        print()
print(len(all_books))
print("\n" + "   " + "=" * 50 + "\n")
