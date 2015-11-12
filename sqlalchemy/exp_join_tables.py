#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, ForeignKey, MetaData)
from sqlalchemy.sql import select


def to_sql(statement):
    return ''.join(str(statement.compile(compile_kwargs={"literal_binds": True})).split('\n'))


eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

with eng.connect() as con:
    meta = MetaData(eng)

    authors = Table('Authors', meta,
                    Column('Id', Integer, primary_key=True),
                    Column('Name', String(40))
                    )
    books = Table('Books', meta,
                  Column('Id', Integer, primary_key=True),
                  Column('Title', String(40)),
                  Column('AuthorId', Integer, ForeignKey("Authors.Id"), nullable=False)
                  )

    if books.exists():
        books.drop()
    if authors.exists():
        authors.drop()

    authors.create()
    books.create()

    stm = authors.insert().values(Id=1, Name='Jesse MENG')
    stm2 = authors.insert().values(Id=2, Name='Jesse MENG')
    con.execute(stm)
    con.execute(stm2)

    stm = books.insert().values(Id=1, Title='Python Programming', AuthorId=1)
    stm2 = books.insert().values(Id=2, Title='Ruby Programming', AuthorId=1)
    stm3 = books.insert().values(Id=3, Title='Lua Programming', AuthorId=2)
    con.execute(stm)
    con.execute(stm2)
    con.execute(stm3)

    # stm = select([books.join(authors)])
    stm = select([authors.join(books)])
    print(to_sql(stm))
    rs = con.execute(stm)

    for row in rs:
        print(row['Name'], row['Title'])
