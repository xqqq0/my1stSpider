#-*-coding:utf-8-*-
import requests
from  requests.exceptions import RequestException
from urllib import urlencode

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

def main():
    html = get_page_index(0,"街拍")
    print html

if __name__ == "__main__":
    main()




