import requests
from lxml import etree
import time

with open("E:\\testfile\\豆瓣音乐top250.txt", "w", encoding="utf-8") as f:
    for i in range(10):
        # 一共有10个页面，每个页面25首音乐
        url = "https://music.douban.com/top250?start={}".format(i * 25)
        headers = {"User_Agent": "Mozilla/5.0(compatible; MSIE 5.5; Windows 8)"}
        data = requests.get(url, headers=headers).text
        s = etree.HTML(data)

        # 歌曲整体的xpath
        musics = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        time.sleep(2)

        for music in musics:
            music_name = music.xpath('./tr/td[2]/div/a/text()')[0].strip()  # 歌名
            music_author = music.xpath('./tr/td[2]/div/p[1]/text()')[0].strip()  # 作者
            music_score = music.xpath('./tr/td[2]/div/div/span[2]/text()')[0]  # 评分
            music_href = music.xpath('./tr/td[2]/div/a/@href')[0]  # 链接

            f.write("{} {} {} {}\n".format(music_name, music_author, music_score, music_href))
