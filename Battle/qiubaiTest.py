import requests
from lxml import etree
import xlwt

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
items = []

def getDivList(page):
    url = 'http://www.qiushibaike.com/hot/page/'+str(page)
    html = requests.get(url, headers=headers).text
    selector = etree.HTML(html)
    divList = selector.xpath('//div[@id="content-left"]/div')
    return divList


def getDivItem(divList):

    for div in divList:
        item = []
        # 用户名
        name = div.xpath('.//h2/text()')[0].replace('\n', '')
        item.append(name)
        # 年龄
        try:
            age = div.xpath('.//div[@class=starts-with(@class,"articleGender")]/text()')[0]
        except:
            age = None

        item.append(age)
        # 性别
        male = div.xpath('.//div[contains(@class,"manIcon")]')
        if male:
            item.append("Male")
        else:
            item.append("Female")

        # 内容
        content = div.xpath('.//div[@class="content"]/span/text()')[0].replace('\n', '')
        item.append(content)
        # 点赞数
        love = div.xpath('.//div[@class="stats"]/span[@class="stats-vote"]/i/text()')[0]
        item.append(love)
        # 评论数
        comments = div.xpath('.//div[@class="stats"]/span[@class="stats-comments"]/a/i/text()')[0]
        item.append(comments)
        items.append(item)
    return items

def saveItems(divItems):
    book = xlwt.Workbook()
    sheet = book.add_sheet("my_sheet")
    row = 0
    for items in divItems:
        col = 0
        for item in items:
            sheet.write(row, col, item)
            col += 1
        row += 1
    book.save('E:\\qsbk.xls')


for page in range(1,30):
    divList = getDivList(page)
    divItems = getDivItem(divList)
    print("第 %d 页抓取完成" % (page))
saveItems(divItems)