#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Cars', meta, autoload=True)

    stm = select([cars])
    print('----')
    print(stm)
    print('----')
    rs = con.execute(stm)

    print(rs.fetchall())
