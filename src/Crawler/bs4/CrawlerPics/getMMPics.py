# -*- encoding: utf-8 -*-
import os
import urllib2
from bs4 import BeautifulSoup

root_url = "http://iyangzi.com/?p=194"
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
