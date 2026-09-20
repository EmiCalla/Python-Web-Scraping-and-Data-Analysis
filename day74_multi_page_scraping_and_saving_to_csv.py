# Day 74 (20-09-2026):
# Back on track after 5 days of university issues,

from day66 import scrap_func, requests
import pandas as pd

all_books = []

homepage = 'http://books.toscrape.com/'

for page in range(1,51):
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
    print()
    print("\n" + "   " + "-" * 100 + "\n")
    print(f"Page {page} scraped successfully.")
    print(f"Page {page} contains {len(result)} books.")
    for book in result:
        print("\n" + "   " + "=" * 50 + "\n")
        print(f"Title : {book['Title']}")
        print(f"Price : {book['Price']}")
        print(f"Rating : {book['Rating']}")
        print(f"Availability : {book['Availability']}")
        print(f"Book_Link : {book['Link']}")
        print()
    print(f"Page {page} end.")
print(len(all_books))
print("\n" + "   " + "=" * 50 + "\n")

df = pd.DataFrame(all_books)
df['Price'] = df['Price'].str.replace('Â£', '')
df['Price'] = df['Price'].astype(float)
df.to_csv('books.csv', index=False)

print(df.shape)
df.info()
