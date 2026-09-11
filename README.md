# Python-Web-Scraping-and-Data-Analysis

# Python Web Scraping and Data Analysis

A learning project documenting my progress with **Python web scraping, data collection, and data analysis using Pandas**.

The project uses [Books to Scrape](https://books.toscrape.com/) as a practice website and gradually develops a scraper while introducing new Python concepts.

## What I Learned

Throughout the project, I worked with:

* Python `requests`
* `BeautifulSoup`
* HTML parsing and element selection
* Extracting data from webpages
* Lists and dictionaries
* Functions and return values
* `append()` vs `extend()`
* Pandas DataFrames
* Exporting data to CSV
* Cleaning and converting scraped data
* Sorting and filtering DataFrames
* Pandas aggregation and grouping
* Basic data analysis
* Multi-page web scraping
* Exception handling with `try` / `except`
* HTTP status checking with `raise_for_status()`
* Request timeouts
* Retry logic
* `break` and `continue`
* Boolean state and control flow

## Project Progress

### Days 50–53 — Basic Web Scraping

Started learning web scraping with `requests` and `BeautifulSoup`.

The scraper extracts basic information about books, including:

* Title
* Price
* Rating

This was the starting point for understanding how HTML structure can be explored and data can be extracted from webpages.

### Day 54 — Storing Scraped Data

Expanded the scraper to collect:

* Title
* Price
* Rating
* Availability
* Link

The extracted data was stored in lists and converted into a Pandas DataFrame.

The DataFrame was then exported to:

`books.csv`

### Day 55 — Dictionaries and Data Cleaning

Changed the data collection approach from multiple separate lists to a list of dictionaries.

The scraped price values were cleaned and converted from strings into floating-point numbers so they could be used for numerical analysis.

### Days 56–58 — Pandas Data Analysis

Used Pandas to explore and analyze the scraped book data.

Some of the operations included:

* Sorting by price and rating
* Filtering books by price
* Finding minimum and maximum prices
* Calculating the average price
* Filtering books by rating
* Counting rating categories
* Descriptive statistics
* Grouping books by rating
* Calculating average, minimum, maximum, median, and count
* Comparing prices to the mean
* Finding books closest to the average price

### Day 59 — Multi-Page Scraping

Extended the scraper from one page to multiple pages.

The scraper collected books from pages 1–5, resulting in up to 100 books.

This introduced the idea of:

```text
Outer loop → pages
Inner loop → books on each page
```

The page URLs were also saved separately.

### Days 61–62 — Functions and Refactoring

Refactored the scraping process into a reusable function:

```text
scrap_func(url)
```

The function takes a URL, scrapes one page, and returns the books from that page.

The overall structure became:

```text
Page URL
    ↓
scrap_func(url)
    ↓
Scrape one page
    ↓
Return that page's list
    ↓
result
    ↓
all_books.extend(result)
    ↓
Master list
```

This helped me understand function inputs, return values, local variables, and the difference between `append()` and `extend()`.

### Days 63–65 — Error Handling and Retry Logic

Added error handling to make the scraper more resilient.

The scraper now uses:

* `response.raise_for_status()`
* `requests.exceptions.Timeout`
* `requests.exceptions.RequestException`
* `timeout=10`
* Retry attempts

Each page can be attempted up to three times.

The control flow is structured so that:

```text
Page
 ↓
Try scraping
 ↓
Success → stop retrying → process page
 ↓
Failure → try again
 ↓
All attempts fail → skip page → continue to next page
```

This was my introduction to designing control flow around real-world failures rather than assuming every request will succeed.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

## Data Source

The project uses **Books to Scrape**, a website specifically designed for practicing web scraping.

## Purpose

This repository is primarily a record of my learning process.

The code is intentionally organized around different stages of learning rather than being presented as a single production-ready scraper. Each stage builds on concepts introduced earlier and documents how my understanding of Python and web scraping is developing.
