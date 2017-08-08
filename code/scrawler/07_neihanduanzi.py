# -*- encoding:utf-8 -*-
'''
    内涵段子爬虫
'''

import re
import urllib2


class NeiHanDuanZiSpider():
    def __init__(self):
        '''
            page:起始页码位置
            switch:控制是否继续爬
        '''
        self.page = 1
        self.switch = True

    def load_page(self):
        '''
            获取网页内容
        '''
        url = "http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list = pattern.findall(html)
        # for content in content_list:
        #     print content.decode("gbk").encode("utf-8")

        self.deal_page(content_list)

    def deal_page(self, content_list):
        '''
            处理每页的数据
        '''
        for item in content_list:
            item = item.replace("<br>", "").replace("<br />", "").replace("<p>", "").replace("</p>", "")
            # print item.decode("gbk")
            self.write_page(item)

    def write_page(self, item):
        '''
            将内容保存到文件中
        '''
        with open("G:\\projects\\MyPythonProject\\file\\NeiHanDuanZi.txt", "a") as f:
            f.write(item.decode("gbk").encode("utf-8"))

    def start_work(self):
        '''
            控制爬虫的运行
        '''
        self.load_page()
        while self.switch:
            command = raw_input("press ENTER to continue, press quit to quit")
            if command == "quit":
                self.switch = False
            self.page += 1


if __name__ == "__main__":
    spider = NeiHanDuanZiSpider()
    # spider.load_page()
    spider.start_work()