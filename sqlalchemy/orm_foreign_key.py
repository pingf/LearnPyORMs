#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine("mysql+pymysql://root:123456@localhost/test0")

Base = declarative_base()
Base.metadata.bind = eng


class Author(Base):
    __tablename__ = "Authors"

    AuthorId = Column(Integer, primary_key=True)
    Name = Column(String(40))
    Books = relationship("Book")


class Book(Base):
    __tablename__ = "Books"

    BookId = Column(Integer, primary_key=True)
    Title = Column(String(40))
    AuthorId = Column(Integer, ForeignKey("Authors.AuthorId"))

    Author = relationship("Author")


authors = Base.metadata.tables['Authors']
books = Base.metadata.tables['Books']
if books.exists():
    books.drop()
if authors.exists():
    authors.drop()
authors.create()
books.create()

Session = sessionmaker(bind=eng)
ses = Session()

a1 = Author(Name='Jesse MENG')
a2 = Author(Name='Anonymous')
b1 = Book(Title='Python Programming', AuthorId=1)
b2 = Book(Title='Ruby Programming', AuthorId=1)
b3 = Book(Title='Lua Programming', AuthorId=2)
ses.add_all([a1, a2, b1, b2, b3])
ses.commit()
#
res = ses.query(Author).filter(Author.Name == "Jesse MENG").first()

for book in res.Books:
    print(book.Title)
#
res = ses.query(Book).filter(Book.Title == "Python Programming").first()
print(res.Author.Name)
