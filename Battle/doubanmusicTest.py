import requests
from lxml import etree


# with open("E:\\testfile\\豆瓣音乐top250.txt","w",encoding='utf-8') as f:
for i in range(1,10):
    url =  "https://music.douban.com/top250?start={}".format(25 * i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    data = requests.get(url,headers=headers).text
    html = etree.HTML(data)
    #这个地方注意，拿到的是25个table
    musics = html.xpath('//*[@id="content"]/div/div[1]/div/table')
    print(musics)