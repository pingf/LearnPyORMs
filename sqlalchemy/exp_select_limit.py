#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")


def to_sql(stm):
    return ''.join(str(stm.compile(compile_kwargs={"literal_binds": True})).split('\n'))


with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Cars', meta, autoload=True)

    stm = select([cars.c.Name, cars.c.Price]).limit(3)
    print('----')
    print(to_sql(stm))
    print('----')
    rs = con.execute(stm)

    print(rs.fetchall())
