#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

Base = declarative_base()
Base.metadata.bind = eng

class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)

Session = sessionmaker(bind=eng)
ses = Session()

rs = ses.query(Car).filter(Car.Name.like('%en'))

for car in rs:
    print(car.Name, car.Price)