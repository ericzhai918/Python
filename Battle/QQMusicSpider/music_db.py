from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/music_db?charset=utf8", echo=False)
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
Base = declarative_base()


class song(Base):
    __tablename__ = 'song'
    song_id = Column(Integer, primary_key=True)
    song_name = Column(String(100))
    song_album = Column(String(100))
    song_interval = Column(String(100))
    song_songmid = Column(String(100))
    song_singer = Column(String(100))

Base.metadata.create_all(engine)

def insert_data(song_dict):
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/music_db?charset=utf8", echo=False)
    DBSession = sessionmaker(bind=engine)
    SQLsession = DBSession()
    data = song(
        song_name=song_dict['song_name'],
        song_album=song_dict['song_album'],
        song_interval=song_dict['song_interval'],
        song_songmid=song_dict['song_songmid'],
        song_singer=song_dict['song_singer'],
    )
    SQLsession.add(data)
    SQLsession.commit()
