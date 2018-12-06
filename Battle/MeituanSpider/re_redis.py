from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from re_food_db import *
import redis

rd = redis.Redis(host='127.0.0.1', port=6379)

# 使用utf8mb4编码连接MySql
engine = create_engine('mysql+pymysql://root:123456@localhost/re_food_db?charset=utf8mb4')
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()


# for instance in SQLsession.query(shop).order_by(shop.id):
#     rd.setnx(instance.shop_id, instance.shop_name)

# a = rd.get(1603003)
# print(a.decode())

# a =from_mysql_to_redis()
# print(a)