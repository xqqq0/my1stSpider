# -*-coding:utf-8-*-
import re

from bs4 import BeautifulSoup
import json
from urllib import urlencode
from requests.exceptions import RequestException
import requests


'''
获取首页的数据
1.经过分析得出，首页的图片数据是通过ajax请求获取，
所以get_page_index构建一个ajax请求，获取数据
'''
def get_page_index(offset,keyword):
    # 参数：从页面的XHR过滤器的header中得到的
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab":" 1"
    }

    # 爬取网页的url,也是从header中得到格式是baseUrl + 参数（参数要编码一下）
    baseUrl = "http://www.toutiao.com/search_content/?"
    url = baseUrl + urlencode(data)

    # 发起请求通过requests框架
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        print("首页索引页面获取失败")
        return None

'''
2.将首页返回的json字符串数进行提取
'''
def parse_page_index(html):
    # 将json字符串转换为json数据，需要import json
    data = json.loads(html)
    #经过分析发现，图片素材是在json的data/image_url节点之下
    ##先判断节点是否存在
    if data and "data" in data.keys():
        ## 如果存在则获取"data"节点的数据
        for item in data.get("data"):
            yield item.get("article_url")

'''
3.获取页面详情页数据，与获取索引页相同，
'''
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        print("页面详情获取失败")
        return None

'''
4.解析详情页面，获取页面数据，由于详情页面的返回的html,故可以通过BS框架去解析
'''

def parse_page_detail(html, url):
    # 获取页面标题，由于线板的标题例子 "时尚牛仔街拍 - 今日头条(www.toutiao.com)"
    # 我们用正则吧 - 今日头条(www.toutiao.com)去掉
    soup = BeautifulSoup(html, "lxml")
    title = soup.select("title")[0].get_text()
    # 经过分析详情页面的数据是在页面的一个js变量(var gallery = )中，故通过正则匹配将之筛选出来
    image_pattern = re.compile('var gallery = (.*?);', re.S)
    match = re.search(image_pattern, html)
    if match:
        #  如果解析成功，就解析返回的json串返回，并获取其中图片的键值
        print(title)
        data = json.loads(match.group(1))
        if data and "sub_images" in data.keys():
            images = [item.get("url") for item in data.get("sub_images")]
            return {
                "title": title,
                "image": images,
                "url": url
            }
    else:
        print("*****")


def main():
    html = get_page_index(0, "街拍")
    for url in parse_page_index(html):
        detail = get_page_detail(url)
        # 这里进行一下判断，如果能正常返回在进行解析
        if detail:
            print (parse_page_detail(detail, url))
if __name__ == "__main__":
    main()




