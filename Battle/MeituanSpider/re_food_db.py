import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 使用utf8mb4编码连接MySql
engine = create_engine('mysql+pymysql://root:123456@localhost/re_food_db?charset=utf8mb4')
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
Base = declarative_base()

# 商家数据表
class shop(Base):
    __tablename__ = 'meituan_shop'
    id = Column(Integer(), primary_key=True)
    shop_id = Column(String(100), comment='商家ID')
    shop_name = Column(String(300), comment='商家名称')
    shop_address = Column(String(500), comment='商家地址')
    shop_phone = Column(String(100), comment='商家电话')
    shop_openTime = Column(String(500), comment='营业时间')
    shop_avgScore = Column(String(100), comment='评分')
    shop_avgPrice = Column(String(100), comment='人均价格')
    shop_city = Column(String(100), comment='所在城市')
    log_date = Column(String(100), comment='记录日期')
    shop_latitude = Column(String(100), comment='纬度')
    shop_longitude = Column(String(100), comment='经度')

# 创建数据表
Base.metadata.create_all(engine)

# 写入商家信息
def shop_db(info_dict):
    # temp_id = info_dict['shop_id']
    # # 判断是否已存在记录
    # info = SQLsession.query(shop).filter_by(shop_id=temp_id).first()
    # if info:
        # info.shop_id = info_dict.get('shop_id', '')
        # info.shop_name = info_dict.get('shop_name', '')
        # info.shop_address = info_dict.get('shop_address', '')
        # info.shop_phone = info_dict.get('shop_phone', '')
        # info.shop_openTime = info_dict.get('shop_openTime', '')
        # info.shop_avgScore = info_dict.get('shop_avgScore', '')
        # info.shop_avgPrice = info_dict.get('shop_avgPrice', '')
        # info.shop_city = info_dict.get('shop_city', '')
        # info.log_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # info.latitude = info_dict.get('shop_latitude', '')
        # info.longitude = info_dict.get('shop_longitude', '')
    #     pass
    #
    # else:
    inset_data = shop(
        shop_id=info_dict.get('shop_id', ''),
        shop_name=info_dict.get('shop_name', ''),
        shop_address=info_dict.get('shop_address', ''),
        shop_phone=info_dict.get('shop_phone', ''),
        shop_openTime=info_dict.get('shop_openTime', ''),
        shop_avgScore=info_dict.get('shop_avgScore', ''),
        shop_avgPrice=info_dict.get('shop_avgPrice', ''),
        shop_city=info_dict.get('shop_city', ''),
        log_date=time.strftime('%Y-%m-%d', time.localtime(time.time())),
        shop_latitude = info_dict.get('shop_latitude', ''),
        shop_longitude=info_dict.get('shop_longitude', ''),
        )
    SQLsession.add(inset_data)
    SQLsession.commit()


