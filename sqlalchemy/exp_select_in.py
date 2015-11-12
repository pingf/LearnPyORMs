#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData, tuple_
from sqlalchemy.sql import select


def to_sql(statement):
    return ''.join(str(statement.compile(compile_kwargs={"literal_binds": True})).split('\n'))


eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Cars', meta, autoload=True)

    k = [(2, ''), (4, 'Volvo'), (6, ''), (8, '')]
    stm = select([cars]).where(tuple_(cars.c.Id, cars.c.Name).in_(k))
    print('----')
    print(to_sql(stm))
    print('----')
    rs = con.execute(stm)

    for row in rs:
        print(row['Id'], row['Name'], row['Price'])

    k = [(2, ), (4, ), (6, ), (8, )]
    stm = select([cars]).where(tuple_(cars.c.Id).in_(k))
    print('----')
    print(to_sql(stm))
    print('----')
    rs = con.execute(stm)

    for row in rs:
        print(row['Id'], row['Name'], row['Price'])
