# -*- coding: utf-8 -*-


import urllib2
import re

# 当前的博客列表页号
page_num = 1
# 不是最后列表的一页，如果有尾页说明不是最后一页
notLast = 1

account = raw_input("访问的用户名：")

# 首页地址
baseUrl = 'http://blog.csdn.net/'+account

while notLast:
    # 连接页号，组成爬取的页面网址
    myUrl = baseUrl+'/article/list/' + str(page_num)

    # 伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)'
    headers = {'User-Agent': user_agent}

    # 构造请求
    req = urllib2.Request(baseUrl, headers=headers)

    # 访问页面
    try:
        myResponse = urllib2.urlopen(req)  # timeout用来设置超时
    except Exception, e:
        raise
    else:
        pass  # Python pass是空语句，是为了保持程序结构的完整性。
    finally:
        pass

    myPage = myResponse.read()  # read()

    #output = open('csdn.txt', 'w')
    #output.write(myPage)
    #output.close()

    #print("notLast = " ,str(notLast));

    print '-----------------------------第%d页---------------------------------' % (page_num,)

    # 利用正则表达式来获取博客的标题
    titles = re.findall(
        '<span class="link_title"><a href=".*?">(.*?)</a></span>', myPage, re.S)

    titleList = []  # 表用[ ]标识。是python最通用的复合数据类型
    for items in titles:
        # list.append(obj)：在列表末尾添加新的对象
        titleList.append(str(items).lstrip().rstrip())

    # 利用正则表达式获取博客的访问量
    views = re.findall(
        '<span class="link_view".*?><a href=".*?" title="阅读次数">阅读</a>\((.*?)\)</span>', myPage, re.S)
    viewList = []
    for items in views:
        viewList.append(str(items).lstrip().rstrip())

    # 利用正则表达式获取简述
    simdes = re.findall(
        '<div class="article_description">(.*?)</div>', myPage, re.S)
    textList = []
    for items in simdes:
        textList.append(str(items).lstrip().rstrip())

    # 将结果输出
    for n in range(len(titleList)):
        print '访问量:%s \r\n标题:%s \r\n简述:%s' % (viewList[n].zfill(4), titleList[n], textList[n])

    # 页号加1
    page_num = page_num + 1

    # 在页面中查找是否存在‘尾页’这一个标签来判断是否为最后一页
    notLast = re.findall('<a href=".*?">尾页</a>', myPage, re.S)
