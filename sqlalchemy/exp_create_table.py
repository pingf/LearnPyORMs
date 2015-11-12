#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, MetaData)
from sqlalchemy.sql import select


def to_sql(statement):
    return ''.join(str(statement.compile(compile_kwargs={"literal_binds": True})).split('\n'))


eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Cars', meta,
                 Column('Id', Integer, primary_key=True),
                 Column('Name', String(16)),
                 Column('Price', Integer)
                 )

    if cars.exists():
        cars.drop()
    cars.create()

    ins1 = cars.insert().values(Id=1, Name='Audi', Price=52642)
    print(to_sql(ins1))
    con.execute(ins1)

    ins2 = cars.insert().values(Id=2, Name='Mercedes', Price=57127)
    print(to_sql(ins2))
    con.execute(ins2)

    ins3 = cars.insert().values(Id=3, Name='Skoda', Price=6000)
    print(to_sql(ins3))
    con.execute(ins3)

    s = select([cars])
    rs = con.execute(s)

    for row in rs:
        print(row['Id'], row['Name'], row['Price'])
