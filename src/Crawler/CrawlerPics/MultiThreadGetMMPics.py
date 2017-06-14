# -*- encoding:utf-8 -*-
'''
    使用多线程获取图片
'''

import os
import urllib2
import re
from bs4 import BeautifulSoup


new_urls = set()
crawler_urls = set()
count = 1

dist_dir = "G://MMPics"
if not os.path.exists(dist_dir):
    os.mkdir(dist_dir)
os.chdir(dist_dir)


def get_mm_pics(root_url):
    new_urls.add(root_url)
    while len(new_urls) != 0:
        new_url = new_urls.pop()
        crawler_urls.add(new_urls)
        print new_url

        try:
            response = urllib2.urlopen(new_url)
            if response.code == 200:
                soup = BeautifulSoup(response.read(), 'html.parser')
                urls = soup.find_all('a', {'href' : re.compile(r"http://iyangzi.com/\?p=\d+$")})
                for url in urls:
                    print url['href']
                    if url['href'] not in new_urls and url['href'] not in crawler_urls:
                        new_urls.add(url['href'])

                all_img = soup.find('div', {'class' : 'post-content'}).find_all('img')

                for img in imgs:
                    src = img['src']
                    print src
                    threading.

if __name__ == '__main__':
    root_url = 'http://iyangzi.com/?p=21'
    get_mm_pics(root_url)