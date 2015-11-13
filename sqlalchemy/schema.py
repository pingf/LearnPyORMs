#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, MetaData)

meta = MetaData()
cars = Table('Cars', meta,
             Column('Id', Integer, primary_key=True),
             Column('Name', String),
             Column('Price', Integer)
             )

print("The Name column:")
print(cars.columns.Name)
print(cars.c.Name)

print("Columns: ")
for col in cars.c:
    print(col)

print("Primary keys:")
for pk in cars.primary_key:
    print(pk)

print("The Id column:")
print(cars.c.Id.name)
print(cars.c.Id.type)
print(cars.c.Id.nullable)
print(cars.c.Id.primary_key)

print('-' * 10)
for table in meta.tables:
    print(table)
