"""
book_sampling.py
@author: Yusan Lin
@date: 10/25/2014
"""

# BeautifulSoup
from bs4 import BeautifulSoup

# SoupStrainer
from bs4 import SoupStrainer

# urllib2
import urllib2

books = []

f = open("data/sampling_urls.txt", "rbU")
urls = f.readlines()
for i in range(len(urls)):
    urls[i] = urls[i].replace("\n", "")

for u in urls:
    print u
    print len(books)
    response = urllib2.urlopen(u)
    html = response.read()
    soup = BeautifulSoup(html)
    
    try:
        books.extend([x['href'] for x in soup.find_all("a", class_ = "linked-image book")])
        books.extend([x.find("a")['href'] for x in soup.find_all("li", class_="title")])
        books.extend([x.find("a")['href'] for x in soup.find_all("span", class_="product-title")])
    except TypeError:
        pass


books = list(set(books))

f = open("data/book_urls_1205.txt", "w")
for book in books:
    f.write(str(book) + "\n")
f.close()
