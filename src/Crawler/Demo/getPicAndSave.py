# -*- encoding:utf-8 -*-

'''
    网络图片的爬取和存储
'''

import requests
import os

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1494672815168&di=b16950b534b84e8352e08634335d5ae5&imgtype=0&src=http%3A%2F%2Fwww.wdace.com%2Fhtml%2Fuploads%2Fallimg%2F160225%2F01414S5G-0-lp.jpg'
root = '/Users/iustc/Desktop/Pictures/'
savePath = root + url.split('/')[-1]

print 'savePath',savePath

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(savePath):
        r = requests.get(url_vedio)
        with open(savePath,'wb') as f:
            f.write(r.content)
            f.close()
            print 'file Save Success'
    else:
        print 'file exists'
except:
    print 'Crawler Failed'