# -*- coding: utf-8 -*-
import sqlite3
from bot.config import db


def create_tables():
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE books(id INT, author varchar(50), name varchar(100))")
        cursor.execute("CREATE TABLE user_books(id_user int, id_book int,read bool)")
        cursor.execute("CREATE TABLE user(id int, name varchar(50))")


def add_user(user):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO user VALUES (?,?)", (user.id, user.first_name,))


def add_book(book, author):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO books(author, name) VALUES (?,?)", (author, book.lower()))
        bid, a, name = get_book(book)
        return bid


def add_user_books(user_id, book_id, read):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO user_books VALUES (?,?,?)", (user_id, book_id, read))


def get_books():
    books = []
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("SELECT author, name FROM books")
        result = cursor.fetchall()
        for i in result:
            books.append(i)
        return books


def get_user(user):
    """ мб пригодится, в любом случае тренировочка """
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM user WHERE id = ?", (user.id,))
        unique = cursor.fetchall()
        if unique:
            return unique


def user_exists():
    """ проверка, что такой юзверь есть в БД"""

    # todo: метод sql exists. результат - True или False
    pass


def get_book(book):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM books WHERE name like ?", (f"%{book.lower()}%",))
        unique = cursor.fetchall()
        if unique:
            return unique[0]


def get_book_by_id(id):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
        unique = cursor.fetchall()
        if unique:
            return unique[0]
