#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_


def to_sql(statement):
    return ''.join(str(statement.compile(compile_kwargs={"literal_binds": True})).split('\n'))


eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Cars', meta, autoload=True)

    stm = select([cars.c.Id, cars.c.Name]).where(and_(cars.c.Price > 10000,
                                                      cars.c.Price < 40000,
                                                      cars.c.Id > 4))
    print('----')
    print(to_sql(stm))
    print('----')
    rs = con.execute(stm)

    print(rs.fetchall())
