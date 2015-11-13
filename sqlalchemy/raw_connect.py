#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    rs = con.execute('SELECT 5')
    data = rs.fetchone()[0]
    print("Data: %s" % data)
