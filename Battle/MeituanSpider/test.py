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
# import redis
#
# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('1111', 'aaaaa')
# r.set('2222', 'bbbb')
# r.set('3333', 'cccc')
# print(r.get('1111'))
#
# r.setnx('1111','abc')
# print(r.get('1111'))

# from sqlalchemy import *
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from re_food_db import *
# import redis
#
# r = redis.Redis(host='127.0.0.1', port=6379)
#
# # 使用utf8mb4编码连接MySql
# engine = create_engine('mysql+pymysql://root:123456@localhost/re_food_db?charset=utf8mb4')
# DBSession = sessionmaker(bind=engine)
# SQLsession = DBSession()
#
# def from_mysql_to_redis():
#     for instance in SQLsession.query(shop).order_by(shop.id):
#         r.setnx(instance.shop_id, instance.shop_name)
#     return r
# a = r.get(1603003)
# print(a.decode())

# a =from_mysql_to_redis()
# print(a)

categorize_dict = {'蛋糕甜点': 'c11', '火锅': 'c17', '自助餐': 'c40', '小吃快餐': 'c36',
                   '日本料理': 'c20059', '韩国料理': 'c20060', '西餐': 'c35',
                   '聚餐宴请': 'c395', '东北菜': 'c20003', '烧烤烤肉': 'c54',
                   '川湘菜': 'c55', '江浙菜': 'c56', '香锅烤鱼': 'c20004', '粤菜': 'c57',
                   '中式烧烤/烤串': 'c400', '西北菜': 'c58', '咖啡酒吧': 'c41', '京菜鲁菜': 'c59',
                   '云贵菜': 'c60', '东南亚菜': 'c62', '海鲜': 'c63', '台湾/客家菜': 'c227',
                   '创意菜': 'c228', '汤/粥/炖菜': 'c229', '新疆菜': 'c233', '其他美食': 'c24',
                   '代金券': 'c393'}

for v in categorize_dict.values():
    print(v)