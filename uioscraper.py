#!/usr/bin/python3

import httplib2, re, wget, os
from bs4 import BeautifulSoup

url = input('Enter URL:\n')

headers, body = httplib2.Http().request(url)
soup = BeautifulSoup(body, 'html.parser')
for link in soup.find_all('a', href=re.compile("^{}".format(url))):
    wget.download(link.get('href'), out=os.path.join(os.path.expanduser('~'), 'Downloads/'))
