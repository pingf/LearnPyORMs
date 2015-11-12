#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, asc


def to_sql(statement):
    return ''.join(str(statement.compile(compile_kwargs={"literal_binds": True})).split('\n'))


eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    metadata = MetaData(eng)
    cars = Table('Cars', metadata, autoload=True)

    stm = select([cars]).order_by(asc(cars.c.Name))
    print('----')
    print(to_sql(stm))
    print('----')
    rs = con.execute(stm)

    for row in rs:
        print(row['Id'], row['Name'], row['Price'])
