# import re
# import requests
# import json
# url = 'http://www.meituan.com/meishi/6903956/'
# headers = {
#         'Host': 'www.meituan.com',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
#     }
# r = requests.get(url=url, headers=headers)
# a = re.findall('("\$meta":.*),"crumbNav"',r.text)
#
# ad=json.loads("{%s}" % a[0])
# print(ad['detailInfo'])
# print(ad['detailInfo']['name'])
#
#
# print(ad['recommended'])
# print(len(ad['recommended']))
# l ={}
# for i in ad['recommended']:
#     # l[i['name']] = l[i.get('price',"None")]
#     l[i['name']] = i['price']
#
# print(l)
#

# import time
# import datetime
#
# t = time.time()
# print(t)
# print(int(t))
# print(int(round(t*1000)))
#
# st = time.localtime(1543901662.429062)
# a = time.strftime('%Y-%m-%d %H:%M:%S',st)
# print(a)

# 测试连接redis
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('1111', 'aaaaa')
r.set('2222', 'bbbb')
r.set('3333', 'cccc')
print(r.get('1111'))

r.setnx('1111','abc')
print(r.get('1111'))
