"""
scrape_batch_books.py
"""

import csv

f = open("data/book_urls.txt", "rbU")
urls = f.readlines()
for i in range(len(urls)):
    urls[i] = urls[i].replace("\n", "")
    
import scrape_one_book as sob

data = []
for url in urls:
    print url
    data.append(sob.scrape_book(url))