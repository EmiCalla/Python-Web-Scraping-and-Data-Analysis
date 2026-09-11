# Day 56, 57, and 58(02,03,04-09-2026):

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

df.sort_values(['Price', 'Rating'],ascending=[False, True], inplace=True)
filt_min = df['Price'] == df['Price'].min()
filt_max = df['Price'] == df['Price'].max()
filt_greater_than_mean = df['Price'] > df['Price'].mean()
filt_rating_5 = df['Rating'] == 'Five'
filt_double = (filt_greater_than_mean) & (filt_rating_5)


print("\n" + "   " + "=" * 50 + "\n")
print(df[filt_min])
print()
print(df[filt_max])
print()
print(df[filt_greater_than_mean])
print(df[filt_rating_5])
print(df[filt_double])
print(df.sort_values('Price', ascending=False).head())
print(df[filt_rating_5].sort_values('Price', ascending=True).head(3))
print(df['Availability'].value_counts())
print(df['Price'].describe())
print(df.describe(include='all'))
print(df.groupby('Rating')['Price'].mean())
print(df.groupby('Rating')['Price'].agg([ min, max, 'mean', 'median', 'count' ]))

filt_below_mean = df['Price'] < df['Price'].mean()
total_values = df['Rating'].value_counts()
ratings = df['Rating'].unique()
df['Difference'] = abs(df['Price'] - df['Price'].mean())
diff_min = df.sort_values('Difference')

def percentage(count_value , total_books=len(df)):
    return count_value / total_books * 100

for rating,per_value in  total_values.items():
   print(f'{rating} :  {percentage(per_value)}%')

print(df.groupby('Rating')['Price'].mean().sort_values(ascending=False))
print(filt_below_mean.sum())
print(diff_min.head(1))
print(df.groupby('Rating')['Price'].agg([min, max, 'mean', 'count']))
print(df.groupby('Rating')['Price'].mean().sort_values(ascending=False).head(1))
print(df[filt_rating_5].sort_values('Price', ascending=False).head(3))
print(df.groupby('Rating')['Price'].mean().sort_values().head(1))
print("\n" + "   " + "=" * 50 + "\n")
