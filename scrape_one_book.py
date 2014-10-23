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

# these are the features (attributes)
title = soup.find("h1", class_="milo").get_text().strip()
author = soup.find("a", class_="subtle").get_text().strip()
price = soup.find("div", class_="price hilight").get_text().strip()
#subject

product_detail_box = list(soup.find("div", class_="product-details box").descendants)
publisher = product_detail_box[product_detail_box.index("Publisher: ") + 1]
date = product_detail_box[product_detail_box.index("Publication date: ") + 1]
pages = product_detail_box[product_detail_box.index("Pages: ") + 1]
overview = soup.find_all("div", class_="simple-html")[1].get_text()

# this is our final classification label (ground truth)
rating_text = soup.find("span", class_="stars-large r3h")['title']
rating = rating_text[rating_text.find("of")+3 : rating_text.find("out")-1]