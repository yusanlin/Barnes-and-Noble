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

def scrape_book(u):
    
    # u = "http://www.barnesandnoble.com/w/leaving-time-jodi-picoult/1118138473?ean=9780345544926"
    # u = "http://www.barnesandnoble.com/w/the-innovators-walter-isaacson/1119994534?ean=9781476708690"
    response = urllib2.urlopen(u)
    html = response.read()
    soup = BeautifulSoup(html)
    
    # these are the features (attributes)
    try:
        title = soup.find("h1", class_="milo").get_text().strip()
        author = soup.find("a", class_="subtle").get_text().strip()
        price = soup.find("div", class_="price hilight").get_text().strip()[1:]
        format_tmp = soup.find_all("li", class_="format ")
        format_tmp = [x['data-bntrack'] for x in format_tmp]
        nook = "NOOK Book" in format_tmp
        hardcover = "Hardcover" in format_tmp
        audio = "Audiobook" in format_tmp
        subject = [x.get_text() for x in soup.find("ul", class_="related-categories box").find_all("a")]
        
        product_detail_box = list(soup.find("div", class_="product-details box").descendants)
        publisher = product_detail_box[product_detail_box.index("Publisher: ") + 1]
        date = product_detail_box[product_detail_box.index("Publication date: ") + 1]
        pages = product_detail_box[product_detail_box.index("Pages: ") + 1]
        overview = soup.find_all("div", class_="simple-html")[1].get_text()
        n_reviews = soup.find("div", id = "reviews-sort-controls-1").find_all("strong")[1].get_text()
        
        
        # this is our final classification label (ground truth)
        rating = soup.find("span", itemprop="ratingValue").get_text()
        
        return [title, author, price, nook, hardcover, audio, subject, publisher, date, pages, overview, n_reviews, rating]
    
    except (AttributeError, IndexError, ValueError) as e:
        #print "not complete book. discard."
        return None
