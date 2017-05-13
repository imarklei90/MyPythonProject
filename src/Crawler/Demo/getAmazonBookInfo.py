# -*- encoding:utf-8 -*-
'''
    获取亚马逊图书信息
    注：亚马逊的网站禁止Python爬虫访问，需要伪造User-Agent
'''

import requests

def getAmazonBookInfo(url):
    try:
        # 伪造User-Agent的内容,添加到Headers字段中
        kv = {'User-Agent':'Chrome/10'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print r.text[:10000]
    except:
        print '爬取失败'

if __name__ == '__main__':
    getAmazonBookInfo('https://www.amazon.cn/dp/B06XW4KDXP?_encoding=UTF8&ref_=pc_cxrd_658390051_bestTab_658390051_a_best_1&pf_rd_p=94da1051-36f0-4552-9fee-32a40402274a&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=658390051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=3Q91YSW814W3SMJ7J49R&pf_rd_r=3Q91YSW814W3SMJ7J49R&pf_rd_p=94da1051-36f0-4552-9fee-32a40402274a')
