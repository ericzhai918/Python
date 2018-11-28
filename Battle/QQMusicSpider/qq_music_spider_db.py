from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#初始化数据库连接
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/qq_music_db?charset=utf8", echo=False)
#创建会话对象，用于数据库的操作
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
#创建对象的基类
Base = declarative_base()

#映射数据表
class Song(Base):
    #表名
    __tablename__ = 'song'
    #字段，属性
    song_id = Column(Integer,primary_key=True)
    song_name = Column(String(100))
    song_album = Column(String(100))
    song_interval = Column(String(100))
    song_songmid = Column(String(100))
    song_singer = Column(String(100))
    song_singermid = Column(String(100))
    song_albummid = Column(String(100))
#创建数据表
Base.metadata.create_all(engine)
#数据入库
def insert_data(song_dict):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/qq_music_db?charset=utf8', echo=False)
    DBSession = sessionmaker(bind=engine)
    SQLsession = DBSession()
    #创建新Song对象
    data = Song(
        song_name=song_dict['song_name'],
        song_songmid=song_dict['song_songmid'],
        song_album=song_dict['song_album'],
        song_interval=song_dict['song_interval'],
        song_singer=song_dict['song_singer'],
        song_singermid=song_dict['song_singermid'],
        song_albummid=song_dict['song_albummid'],
    )
    # 添加到session
    SQLsession.add(data)
    #提交即保存到数据库
    SQLsession.commit()
