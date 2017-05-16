# -*- encoding:utf-8 -*-

'''
    获取百度股票信息
'''

import requests
from bs4 import BeautifulSoup
import re
import traceback


def get_stock_html(stock_list_url, code = 'utf-8'):
    try:
        r = requests.get(stock_list_url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def get_stock_list(stock_lists, stock_list_url):
    html = get_stock_html(stock_list_url, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for h in a:
        try:
            stock_lists.append(re.findall(r'[s][hz]\d{6}]',h.attrs['href'])[0])
        except:
            continue


def get_stock_info_list(stock_lists, stock_info_url, save_stock_file):
    for stock in stock_lists:
        stock_url = stock_info_url + + stock + '.html'
        html = get_stock_html(stock_url)
        try:
            if html == "":
                continue
            stock_info_dicts = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_info = soup.find_all('div', attrs={'class','stock-bets'})
            stock_info_dicts.update({'股票名称' : stock_info.find_all(attrs={'class' : 'bets-name'})[0].text.split()[0]})

            key_lists = stock_info.find_all('dt')
            value_lists = stock_info.find_all('dd')
            for s in range(len(key_lists)):
                key = key_lists[s].text
                value = value_lists[s].text
                stock_info_dicts[key] = value

            with open(save_stock_file, 'a', encoding ='utf-8') as f:
                f.write(str(stock_info_dicts) + '\n')
                count = count + 1
                print "\r 当前进度:{:.2f}%".format(count * 100 /len(stock_lists))
        except:
            count = count + 1
            print "\r 当前进度:{:.2f}%".format(count * 100 / len(stock_lists))
            continue

def main():
    # 股票列表
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'

    # 每个股票的详细页面
    stock_info_url = 'https://gupiao.baidu.com/stock/'

    # 保存股票信息的文件及位置
    save_stock_file = 'd://baidu_stock_info.txt'

    # 保存股票信息的列表
    stock_lists = []

    # 获取股票列表
    get_stock_list(stock_lists, stock_list_url)

    # 获取股票详细信息
    get_stock_info_list(stock_lists, stock_info_url, save_stock_file)


main()
