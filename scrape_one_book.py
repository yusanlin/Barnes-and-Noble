"""
scrape_one_book.py
@author: Yusan Lin
@date: 2014/10/23
"""

# BeautifulSoup
from bs4 import BeautifulSoup

# SoupStrainer
from bs4 import SoupStrainer

# urllib2
import urllib2

u = "http://www.barnesandnoble.com/w/leaving-time-jodi-picoult/1118138473?ean=9780345544926"
response = urllib2.urlopen(u)
html = response.read()
soup = BeautifulSoup(html)

title = soup.find("h1", class_="milo").get_text().strip()
author = soup.find("a", class_="subtle").get_text().strip()
price = soup.find("div", class_="price hilight").get_text().strip()
rating_text = soup.find("div", class_="price hilight").get_text()
rating = rating_text[rating_text.find("of")+3 : rating_text.find("out")-1]