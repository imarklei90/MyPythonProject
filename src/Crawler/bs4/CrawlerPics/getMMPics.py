# -*- encoding: utf-8 -*-
import os
import re
import urllib2
from bs4 import BeautifulSoup


def getPic(root_url):
    try:
        response = urllib2.urlopen(root_url)
        if response.code == 200:
            girl_dir = "G:\GirlPics"
            if not os.path.exists(girl_dir):
                os.mkdir(girl_dir)
            os.chdir(girl_dir)

            soup = BeautifulSoup(response.read(), 'html.parser')
            all_img = soup.find("div", attrs={'class': 'post-content'}).find_all('img')
            count = 1
            for img in all_img:
                src = img['src']
                name = "iyangzi" + str(count)
                with open(name + '.jpg', 'ab') as img_object:
                    img_content = urllib2.urlopen(src).read()
                    img_object.write(img_content)
                    img_object.flush()
                count += 1
    except urllib2.URLError, e:
        print e


new_urls = set() # new add urls
crawled_urls = set() # has already crawler urls
count = 1


def getPics(root_url):
    dist_dir = "G:\\YangZiPics"
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    os.chdir(dist_dir)

    new_urls.add(root_url)
    while len(new_urls) != 0:
        new_url = new_urls.pop()
        crawled_urls.add(new_url)
        print new_url
        try:
            response = urllib2.urlopen(new_url)
            if response.code == 200:
                soup = BeautifulSoup(response.read(), 'html.parser')
                urls = soup.find_all('a', attrs={'href':re.compile(r'http://iyangzi.com/\?p=\d+$')})
                for url in urls:
                    if url['href'] not in new_urls and url['href'] not in crawled_urls:
                        new_urls.add(url['href'])
                all_imgs = soup.find('div', {'class':'post-content'}).find_all('img')
                count = 0
                for img in all_imgs:
                    src = img['src']
                    name = 'iyangzi_' + str(count)
                    with open(name + ".jpg", 'ab') as img_object:
                        img_content = urllib2.urlopen(src).read()
                        img_object.write(img_content)
                        img_object.flush()
                    count += 1
        except urllib2.URLError, e:
            print e


if __name__ == '__main__':
    root_url = "http://iyangzi.com/?p=73"
    # getPic(root_url)

    getPics(root_url)

