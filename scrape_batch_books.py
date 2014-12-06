"""
scrape_batch_books.py
"""

import csv
import sys

def start():
    f = open("data/book_urls_1205.txt", "rbU")
    urls = f.readlines()
    for i in range(len(urls)):
        urls[i] = urls[i].replace("\n", "")
        
    import scrape_one_book as sob

    f = open("result_1206.txt", "w")
    total = len(urls)
    count = 0
    data = []
    for url in urls:
        #print url
        tmp = sob.scrape_book(url)
        data.append(tmp)
        f.write(str(tmp) + "\n")
        count += 1
        progress = float(count)/total * 100
        sys.stdout.write("\r%20f%%" % progress)
        sys.stdout.flush()

    return data

"""
import pickle
pickle.dump(data, open("book_data_1206.p", "w"))
"""
