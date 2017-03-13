#-*-coding:utf-8-*-
import json
from urllib import urlencode
from  requests.exceptions import RequestException
import requests


'''
获取首页的数据
1.讲过分析得出，首页的图片数据是通过ajax请求获取，
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
        return response.text
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

def main():
    html = get_page_index(0,"街拍")
    for url in parse_page_index(html):
        print(url)

if __name__ == "__main__":
    main()




