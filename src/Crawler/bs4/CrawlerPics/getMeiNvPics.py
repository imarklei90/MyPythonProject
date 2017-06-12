import os
import urllib2
from bs4 import BeautifulSoup


def getMvPics(url):
    try:
        response = urllib2.urlopen(url)
        if response.code == 200:
            dist_dir = "G://MeiNv"
            if not os.path.exists(dist_dir):
                os.mkdir(dist_dir)
            os.chdir(dist_dir)

        soup = BeautifulSoup(response.read(),'html.parser')
        img_all = soup.find('div', {'class': 'lb_box'}).find_all('img')

        count = 0
        for img in img_all:
            src = img['src']
            name = "MeiNv" + str(count)
            with open(name + '.jpg', "wb") as img_object:
                img_content = urllib2.urlopen(src).read()
                img_object.write(img_content)
                img_object.flush()
            count += 1
    except urllib2.URLError, e:
        print e

if __name__ == '__main__':
    url = "http://pic.yesky.com/c/6_61091.shtml"
    getMvPics(url)