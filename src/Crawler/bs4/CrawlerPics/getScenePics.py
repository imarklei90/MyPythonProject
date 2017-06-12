# -*- encoding:utf-8 -*-

import os
import urllib2
from bs4 import BeautifulSoup


def getPics(url):
    try:
        response = urllib2.urlopen(url)
        if response.code == 200:
            dist_pic = "G:\GirlPics"
            if not os.path.exists(dist_pic):
                os.mkdir(dist_pic)
        os.chdir(dist_pic)

        soup = BeautifulSoup(response.read(), 'html.parser')
        all_img = soup.find('ul', attrs={"class": "pli"}).find_all('img')

        count = 0
        for img in all_img:
            src = img['src']
            name = "PoBu" + str(count)
            with open(name + '.jpg', 'ab') as img_object:
                img_content = urllib2.urlopen(src).read()
                img_object.write(img_content)
                img_object.flush()
            count += 1
    except urllib2.URLError, e:
        print e

if __name__ == '__main__':
    url = "http://www.ivsky.com/tupian/pubu_v41524/"
    getPics(url)
