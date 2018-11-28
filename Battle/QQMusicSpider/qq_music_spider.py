import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import math

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

session = requests.session()

def download(guid, songmid,cookie_dict):
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0'\
          '&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%'\
          '3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%22'+ guid + '%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22'\
          '%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%'\
            '22%3A%7B%22guid%22%3A%22'+ guid + '%22%2C%22songmid%22%3A%5B%22' + songmid + '%22%5D%2C%22songtype%22%3A%5B0%5D%2'\
            'C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22'\
            'format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D'
    r = session.get(url, headers=headers, cookies=cookie_dict)
    purl = r.json()['req_0']['data']['midurlinfo'][0]['purl']
    if purl:
        url = "http://dl.stream.qqmusic.qq.com/%s" % (purl)
        print(url)
        r = requests.get(url, headers=headers)
        f = open('E:\\Pythontest1\\song\\' + songmid + '.m4a', 'wb')
        f.write(r.content)
        f.close()
        return True
    else:
        return False

def getCookies():
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=' \
          'utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid=0025NhlN2yWrP4&order=listen&begin=0&num=30&songstatus=1'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://y.qq.com/')
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    one_cookie = driver.get_cookies()
    driver.quit()
    print(one_cookie)
    cookie_dict = {}
    for i in one_cookie:
        cookie_dict[i['name']] = i['value']
    return cookie_dict

def get_singer_songs(singermid,cookie_dict):
    #此url用于动态设置歌手的 singermid，获取歌曲总数和歌手姓名
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&'\
          'notice=0&platform=yqq&needNewCode=0&singermid=%s&order=listen&begin=0&num=30&songstatus=1' %(singermid)
    r = session.get(url)
    song_singer = r.json()['data']['singer_name']
    songcount = r.json()['data']['total']
    pagecount = math.ceil(int(songcount)/30)
    for p in range(pagecount):
        #此url用于动态设置页数，获取当前歌手每一页的歌曲信息
        url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&' \
              'notice=0&platform=yqq&needNewCode=0&singermid=%s&order=listen&begin=%s&num=30&songstatus=1' % (singermid, p * 30)
        r = session.get(url)
        music_data = r.json()['data']['list']
        song_dict = {}
        for i in music_data:
            song_dict['song_name'] = i['musicData']['songname']
            song_dict['song_album'] = i['musicData']['albumname']
            song_dict['song_interval'] = i['musicData']['interval']
            song_dict['song_songmid'] = i['musicData']['songmid']
            song_dict['song_singer'] = song_singer

            download(cookie_dict['pgv_pvid'],song_dict['song_songmid'],cookie_dict)
            song_dict = {}

def get_genre_singer(index,page_list,cookie_dict):
    pass

if __name__ == '__main__':
    cookie_dict = getCookies()
    get_singer_songs('0025NhlN2yWrP4',cookie_dict)

