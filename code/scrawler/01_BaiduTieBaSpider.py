# -*- encoding:utf-8 -*-
'''
    获取贴吧数据
    http://tieba.baidu.com/f?kw=kw&pn=100
'''

import urllib
import urllib2


def baidu_spider(url, start_page, end_page):
    '''
        :param url: 贴吧的url
        :param start_page: 起始页
        :param end_page:结束页
    '''
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        full_url = url + "&pn=" + str(pn)
        file_name = "第" + str(page) + "页"
        # print full_url
        html = send_request(full_url, file_name)
        save_html(html, file_name)


def send_request(url, file_name):
    """
        :param url: 贴吧的URL
        :param file_name: 保存的文件名
    """
    print "正在下载" + file_name
    headers= {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def save_html(html, file_name):
    '''
        :param html: 获取到的页面
        :param file_name: 文件名
    '''
    print "保存文件：" + file_name
    with open("G:\\projects\\MyPythonProject\\file\\" + file_name, "w") as f:
        f.write(html)
        print html
    print "保存完成"

if __name__ == '__main__':
    kw = raw_input("请出入要查询的贴吧的名称：")
    start_page = int(raw_input("请输入起始页码："))
    end_page = int(raw_input("请输入结束的页码："))

    query = urllib.urlencode({"kw" : kw})
    url = "http://tieba.baidu.com/f?" + query

    baidu_spider(url, start_page, end_page)