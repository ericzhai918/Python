import requests
from lxml import etree
import time
import re
import xlwt

items = []
for i in range(0,10):
    url =  "https://music.douban.com/top250?start={}".format(25 * i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    data = requests.get(url,headers=headers).text
    html = etree.HTML(data)
    # 歌曲整体的xpath
    musics = html.xpath('//*[@id="content"]/div/div[1]/div/table')

    for music in musics:
        music_name = music.xpath('./tr/td[2]/div/a/text()')[0].strip()
        music_author = music.xpath('./tr/td[2]/div/p/text()')[0].split('/')[0]
        music_score = music.xpath('./tr/td[2]/div/div/span[2]/text()')[0]
        music_num = music.xpath('./tr/td[2]/div/div/span[3]/text()')[0].split()[1][:-3]
        items.append([music_name,music_author,music_score,music_num])




book = xlwt.Workbook()
sheet = book.add_sheet("my_sheet")
row = 0
for item in items:
    col = 0
    for a in item:
        sheet.write(row, col, a)
        col += 1
    row += 1
book.save('E:\\testfile\\db.xls')
