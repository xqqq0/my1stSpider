# 前言
> 本博客主要记录跟随崔庆才老师的[分析Ajax抓取今日头条街拍美图](https://edu.hellobi.com/course/156/play/lesson/2452)学习的整个过程，更多精品文章，请参阅崔老师的[博客](http://cuiqingcai.com/)，再次感谢崔老师教导。

> 3月15日更新，14日代码敲完了，今天主要总结整个过程

# 啰嗦心得
* 个人觉得在掌握了Python的基础的前提下，爬虫的难点在于两点：
  * 分析网页结构，看要获取的数据获取的方式
  * 利用语言知识去匹配或者利用其它的方法，比如ajax等发起请求获取数据等等

* 这两点前者更为复杂，因为有的网页比如本例中，街拍的索引页面的详情页面中，详情的数据是在页面的一个js的变量中，但是在我跟随视频学习的过程中发现，此时的页面很多已经不是存在一个变量中，而是存在于标签中，说明页面是有过改版，此时同一个详情页面就不能一概而论，要写不同的方法处理，不过由于爬虫功底还很薄弱，所以对于存在于标签中的链接，我并没有处理，而是进行了过滤，待到基础比较扎实以后，会对代码进行更新（`March 15`）

# 开始爬取
### 索引页面
* 前期要求
> 简单来说此次抓取氛围两部分，一部分是图片的索引页面，另外一部分是通过点击索引进入详情页面，抓取具体的图片的地址，并将其存储，最后下载图片资源

*  索引页面分析
> 跟随视频学习，打开谷歌的工具查看索引页面的源代码，没有看到和素材相关的资源，这里略总结一下，以目前自己所学的这点知识，想要的链接信息主要存在于一下三方面的元素中

  * 存在于HTML的标签的链接中
  * 存在于CSS样式中
  * 存在于 页面的js代码中
  * 存在于ajax的请求中（索引页面就是这种）

* 索引页数据分析
  * 通过分析所以页面是通过ajax请求获取到的，通过Google浏览器的工具filter工具的XHR过滤项可以看出
![xhr.png](http://upload-images.jianshu.io/upload_images/954728-b51f82a5a0a4909c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 索引页面数据分析，参看下图
![data](http://upload-images.jianshu.io/upload_images/954728-2129daf129d2bc2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![具体索引链接](http://upload-images.jianshu.io/upload_images/954728-669918cdb0f186c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 经过分析是通过ajax请求，获取回来的数据，其中article_url就是进入详情页面的链接，我们通过构建一个ajax请求，然后获取返回数据，在获取字段
* 索引页抓取 
  * 构建ajax请求获取数据
   * 代码 <b>`由于markdown格式问题，我就不粘贴代码，用图片代替，博客末尾我会附上代码地址`
![索引页面数据获取](http://upload-images.jianshu.io/upload_images/954728-1c049286038e71e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 代码分析 
    * data：是ajax的所需要的参数，这个参数是参看XHR中的
![参数](http://upload-images.jianshu.io/upload_images/954728-3d014b0cca5cbdea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    * url : baseUrl + 经过转码的参数，成为完整的url【get请求】，其中转码函数urlencode包含在你`from urllib import urlencode`
    * 请求：本次的请求框架是requests，我一直以为requests是Python的原生库，其实属于第三方框架 ，故安装`sudo pip install requests  `,导入`import requests`,具体访问参见代码

  * 解析索引页面返回的json数据
    * 根据之前的分析，ajax请求返回值的数据类型是json，故利用Python内部的json模块就可以解析`import json`
    * json 解析完成以后，就可以根据节点取出相应的值，通过遍历数据返回一个首页的索引的ur列表
![索引数据解析](http://upload-images.jianshu.io/upload_images/954728-d54f52ace91fbc5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 详情页面
* 详情页面分析
> 经过分析，在图片的详情页面图片数据是存储在页面的 `var gallery `变量中，这变量后面也是一个json数据，所以我们经过正则匹配来或者这个变量后边的json数据
![](http://upload-images.jianshu.io/upload_images/954728-eaa0402ae29e9fb3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  * 详情页面抓取
这个比较简单，根据索引页的url,进行页面获取，与索引页的获取基本相同
![详情页面获取](http://upload-images.jianshu.io/upload_images/954728-4b259daed8e106f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 详情页面解析
这里要做的工作就是在页面中通过正则匹配找到`var gallery `，然后获取后面的json数据
![gallery后边的json数据结构](http://upload-images.jianshu.io/upload_images/954728-1d0f13300939276f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![详情页面解析](http://upload-images.jianshu.io/upload_images/954728-b00141782101c35b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    * 由于详情页面就是普通的HTML页面，可以通过BeautifulSoup框架解析， BeautifulSoup框架需要通过pip安装，然后导入`from bs4 import BeautifulSoup`
   * 将匹配完获取的数据用json框架进行解析，由于图片数据是一个数组，故需要遍历取值
    * 返回一个数组，包括详情页面的标题，详情页面的url，图片的url数组
 
# 存储到数据库
* 下载安装mongoDB，这里不赘述
* 配置mongoDB，可以参见我的[博客](http://www.jianshu.com/p/f79b759988d3)
* pycharm配置mongoDB
  * 创建config.py配置文件，然后配置一些参数，包括主机，数据库名，表名
![](http://upload-images.jianshu.io/upload_images/954728-441695093f1c791e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 创建数据库，主要利用`pymongo(import pymongo)`框架，因为研究的不是很彻底，这里只写一些简单的代码，不要忘记导入配置文件`from config import *`
![创建数据库](http://upload-images.jianshu.io/upload_images/954728-4885239e18b3a43a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  * 存储数据 
![存储数据](http://upload-images.jianshu.io/upload_images/954728-365a654d8a5573bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 下载图片
*  通过url下载图片数据，是Python相关知识，不赘述
![下载图片](http://upload-images.jianshu.io/upload_images/954728-17c7e77c81f2262c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 将图片数据转换为图片
![转换数据](http://upload-images.jianshu.io/upload_images/954728-cf415a9e4df65f31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 将以上代码整体串接调用
```
def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        detail = get_page_detail(url)
        # 这里进行一下判断，如果能正常返回在进行解析
        if detail and parse_page_detail(detail, url):
            result = parse_page_detail(detail, url)
            if result:
                save_to_db(result)

if __name__ == "__main__":
       main()
```
[代码地址](https://github.com/xqqq0/my1stSpider)

# 最后
> 无论从接触爬虫还是博客的编写都显得匆忙和粗糙，以后随着知识的完善，博客也会进行相应的更新，希望大家不吝赐教，提出问题指正，谢谢