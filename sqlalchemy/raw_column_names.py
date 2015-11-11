#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.sql import text

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    rs = con.execute(text('SELECT * FROM Cars'))
    print(rs.keys())
    for r in rs:
        print(r)
