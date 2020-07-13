import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 使用utf8mb4编码连接MySql
engine = create_engine('mysql+pymysql://root:123456@localhost/war_db?charset=utf8mb4')
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
Base = declarative_base()


# 用户信息表
class User(Base):
    __tablename__ = 'user200214'
    id = Column(Integer(), primary_key=True)
    user_id = Column(String(100), comment='用户ID')
    user_name = Column(String(300), comment='用户昵称')
    user_content = Column(String(5000), comment='个人信息')
    user_profile = Column(String(500), comment='用户头像')
    user_pic = Column(String(5000), comment='用户照片')
    user_createTime = Column(String(100), comment='用户上传时间')


# 创建数据表
Base.metadata.create_all(engine)


# 写入用户信息
def insert_data(info_box):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/war_db?charset=utf8', echo=False)
    DBSession = sessionmaker(bind=engine)
    SQLsession = DBSession()
    # 创建新User对象
    data = User(
        user_id=info_box.get('user_id', ''),
        user_name=info_box.get('user_name', ''),
        user_content=info_box.get('user_content', ''),
        user_profile=info_box.get('user_profile', ''),
        user_pic=' '.join(info_box.get('user_pic', '')),
        user_createTime=info_box.get('user_createTime', ''),
    )
    # 添加到session
    SQLsession.add(data)
    # 提交即保存到数据库
    SQLsession.commit()
