import requests 
from bs4 import BeautifulSoup

def scrap_func(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    dic_list = []
    for book in books:
            title_element = book.find('img')
            if title_element is None:
                title = None
            else:
                title = title_element['alt']

            link_element = book.find('h3')
            if link_element is None:
                link = None
            else:
                link_tag = link_element.find('a')
                if link_tag is None:
                    link = None
                else:
                    link = link_tag['href']

            product_price = book.find('div', class_='product_price')
            if product_price is None:
                price = None
            else:
                price = product_price.p.text

            product_rating = book.find('p', class_='star-rating')
            if product_rating is None:
                rating = None
            else:
                 rating = product_rating['class'][1]

            availability_check = book.find('p', class_='instock availability')
            if availability_check is None:
                availability = None
            else:
                 availability = availability_check.text.strip()

            dic_list.append({'Title' : title,
            'Price' : price,
            'Rating' : rating,
            'Availability' : availability,
            'Link': link})
    return dic_list