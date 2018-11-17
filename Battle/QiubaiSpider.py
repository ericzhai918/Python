import os
import re
import requests
from lxml import etree


# 糗事百科爬虫
class QSBK:
    # 初始化方法，定义变量
    def __init__(self):
        self.pageIndex = 1
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
        }
        self.enable = False

    # 返回页面的div_list
    def getHtmlDivList(self, pageIndex):
        pageUrl = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        html = requests.get(url=pageUrl, headers=self.headers).text
        selector = etree.HTML(html)
        divList = selector.xpath('//div[@id="content-left"]/div')
        return divList

    # 获取文本中要截取的元素
    def getHtmlItems(self, divList):

        items = []

        for div in divList:
            item = []
            # 发布人
            name = div.xpath('.//h2/text()')[0].replace("\n", "")
            item.append(name)

            # 内容(阅读全文)
            contentForAll = div.xpath('.//div[@class="content"]/span[@class="contentForAll"]')
            if contentForAll:
                contentForAllHref = div.xpath('.//a[@class="contentHerf"]/@href')[0]
                contentForAllHref = "https://www.qiushibaike.com" + contentForAllHref
                contentForAllHrefPage = requests.get(url=contentForAllHref).text
                selector2 = etree.HTML(contentForAllHrefPage)
                content = selector2.xpath('//div[@class="content"]/text()')
                content = "".join(content)
                content = content.replace("\n", "")
            else:
                content = div.xpath('.//div[@class="content"]/span/text()')
                content = "".join(content)
                content = content.replace("\n", "")
            item.append(content)

            # 点赞数
            love = div.xpath('.//span[@class="stats-vote"]/i[@class="number"]/text()')
            love = love[0]
            item.append(love)

            # 评论人数
            num = div.xpath('.//span[@class="stats-comments"]//i[@class="number"]/text()')
            num = num[0]
            item.append(num)

            items.append(item)

        return items

    # 保存入文本
    def saveItem(self, items):
        f = open('E:\\Pythontest1\\qiushi.txt', "a", encoding='UTF-8')

        for item in items:
            name = item[0]
            content = item[1]
            love = item[2]
            num = item[3]

            # 写入文本
            f.write("发布人：" + name + '\n')
            f.write("内容：" + content + '\n')
            f.write("点赞数：" + love + '\t')
            f.write("评论人数：" + num)
            f.write('\n\n')

        f.close()

    # 判断文本是否已创建，添加路径
    def judgePath(self):
        if os.path.exists('E:\\Pythontest1') == False:
            os.mkdir('E:\\Pythontest1')
        if os.path.exists("E:\\Pythontest1\\qiushi.txt") == True:
            os.remove("E:\\Pythontest1\\qiushi.txt")

    def start(self):
        self.judgePath()
        print("正在读取糗事百科,按回车继续保存下一页，Q退出")
        self.enable = True
        while self.enable:
            divList = self.getHtmlDivList(self.pageIndex)
            data = self.getHtmlItems(divList)
            self.saveItem(data)
            print('已保存第%d页的内容' % self.pageIndex)
            pan = input('是否继续保存：')
            if pan != 'Q':
                self.pageIndex += 1
                self.enable = True
            else:
                print('程序运行结束！！')
                self.enable = False


spider = QSBK()
spider.start()
