# -*- coding: utf-8 -*-
from bot.config import DB
import sqlite3


def create_tables(DB):
    with sqlite3.connect(DB) as con:
        cursor=con.cursor()
        cursor.execute("CREATE TABLE books(id INT, author varchar(50), name varchar(100))")
        cursor.execute("CREATE TABLE user_books(id_user int, id_book int,read bool)")
        cursor.execute("CREATE TABLE user(id int,name varchar(50))")


def add_user(DB, user):
    with sqlite3.connect(DB) as con:
        cursor=con.cursor()
        cursor.execute("INSERT INTO user VALUES (?,?)", (user.id, user.first_name,))

def add_book(DB,book, author):
    with sqlite3.connect(DB) as con:
        cursor=con.cursor()
        cursor.execute("INSERT INTO books(author, name) VALUES (?,?)", (author, book))

def add_user_books(DB, user_id, book_id):
    with sqlite3.connect(DB) as con:
        cursor=con.cursor()
        cursor.execute("INSERT INTO user_books VALUES (?,?,?)", (user_id, book_id))


def get_books(DB):
    books=[]
    with sqlite3.connect(DB) as con:
        cursor=con.cursor()
        cursor.execute("SELECT author,name FROM books")
        result=cursor.fetchall()
        for i in result:
            books.append((i))
        return books


print(get_books(DB))

