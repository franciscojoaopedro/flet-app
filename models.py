from  sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Float
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import  sessionmaker


connection="sqlite:///app_flet.db"
engine=create_engine(connection,echo=True)
Session=sessionmaker(bind=engine)
Session=Session()
Base=declarative_base()

class Produto(Base):
    __tablename__="Produto"
    id=Column(Integer,primary_key=True)
    titulo=Column(String(50))
    preco=Column(Float())

Base.metadata.create_all(engine)
