# my1stSpider

# 
> [Ajax](https://edu.hellobi.com/course/156/play/lesson/2452)[](http://cuiqingcai.com/)

> 31514

# 
* Python
  * 
  * ajax

* js`March 15`

# 
### 
* 
> 

*  
> 

  * HTML
  * CSS
  *  js
  * ajax

* 
  * ajaxGooglefilterXHR
![xhr.png](http://upload-images.jianshu.io/upload_images/954728-b51f82a5a0a4909c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 
![data](http://upload-images.jianshu.io/upload_images/954728-2129daf129d2bc2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](http://upload-images.jianshu.io/upload_images/954728-669918cdb0f186c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * ajaxarticle_urlajax
*  
  * ajax
   *  <b>`markdown`
![](http://upload-images.jianshu.io/upload_images/954728-1c049286038e71e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  *  
    * dataajaxXHR
![](http://upload-images.jianshu.io/upload_images/954728-3d014b0cca5cbdea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    * url : baseUrl + urlgeturlencode`from urllib import urlencode`
    * requestsrequestsPython `sudo pip install requests  `,`import requests`,

  * json
    * ajaxjsonPythonjson`import json`
    * json ur
![](http://upload-images.jianshu.io/upload_images/954728-d54f52ace91fbc5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 
* 
>  `var gallery `jsonjson
![](http://upload-images.jianshu.io/upload_images/954728-eaa0402ae29e9fb3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  * 
url,
![](http://upload-images.jianshu.io/upload_images/954728-4b259daed8e106f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 
`var gallery `json
![galleryjson](http://upload-images.jianshu.io/upload_images/954728-1d0f13300939276f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](http://upload-images.jianshu.io/upload_images/954728-b00141782101c35b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    * HTMLBeautifulSoup BeautifulSouppip`from bs4 import BeautifulSoup`
   * json
    * urlurl
 
# 
* mongoDB
* mongoDB[](http://www.jianshu.com/p/f79b759988d3)
* pycharmmongoDB
  * config.py
![](http://upload-images.jianshu.io/upload_images/954728-441695093f1c791e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * `pymongo(import pymongo)``from config import *`
![](http://upload-images.jianshu.io/upload_images/954728-4885239e18b3a43a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  *  
![](http://upload-images.jianshu.io/upload_images/954728-365a654d8a5573bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 
*  urlPython
![](http://upload-images.jianshu.io/upload_images/954728-17c7e77c81f2262c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 
![](http://upload-images.jianshu.io/upload_images/954728-cf415a9e4df65f31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 
```
def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        detail = get_page_detail(url)
        # 
        if detail and parse_page_detail(detail, url):
            result = parse_page_detail(detail, url)
            if result:
                save_to_db(result)

if __name__ == "__main__":
       main()
```
[](https://github.com/xqqq0/my1stSpider)

# 
> 