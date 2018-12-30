#!/usr/bin/python3

import httplib2, re, wget, os, sys
from urllib import parse
from bs4 import BeautifulSoup

url = sys.argv[1]

headers, body = httplib2.Http().request(url)
url, sep, tail = url.partition('?')
soup = BeautifulSoup(body, 'html.parser')
paths = []

for link in soup.find_all('a', href=re.compile('^{}.+\\..+'.format(url))):
    path = parse.unquote(link.get('href'))
    path, sep, tail = path.partition('?')
    if path not in paths:
        paths.append(path)
        wget.download(path, out=os.path.join(os.path.expanduser('~'), 'Downloads/'))

print('\n{} files found.'.format(len(paths)))