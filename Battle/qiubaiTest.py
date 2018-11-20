import requests
from lxml import etree

url = 'http://www.qiushibaike.com/hot/page/2'
html = requests.get(url).text
selector = etree.HTML(html)
divList = selector.xpath('//div[@id="content-left"]/div')
print(divList)
items = []

for div in divList:
    item = []
    #用户名
    name =div.xpath('.//h2/text()')[0].replace('\n','')
    item.append(name)
    #年龄
    try:
        age = div.xpath('.//div[@class=starts-with(@class,"articleGender")]/text()')[0]
    except:
        age = None

    item.append(age)
    #性别
    male = div.xpath('.//div[contains(@class,"manIcon")]')
    if male:
        item.append("Male")
    else:
        item.append("Female")

    #内容
    content = div.xpath('.//div[@class="content"]/span/text()')[0].replace('\n','')
    item.append(content)
    #点赞数
    love = div.xpath('.//div[@class="stats"]/span[@class="stats-vote"]/i/text()')[0]
    item.append(love)
    #评论数
    comments = div.xpath('.//div[@class="stats"]/span[@class="stats-comments"]/a/i/text()')[0]
    item.append(comments)

    print(item)




