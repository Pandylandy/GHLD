# -*- coding: utf-8 -*-
import sqlite3


def create_tables(db):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE books(id INT, author varchar(50), name varchar(100))")
        cursor.execute("CREATE TABLE user_books(id_user int, id_book int,read bool)")
        cursor.execute("CREATE TABLE user(id int,name varchar(50))")


def add_user(db, user):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO user VALUES (?,?)", (user.id, user.first_name,))


def add_book(db, book, author):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO books(author, name) VALUES (?,?)", (author, book))


def add_user_books(db, user_id, book_id):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO user_books VALUES (?,?,?)", (user_id, book_id))


def get_books(db):
    books = []
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        cursor.execute("SELECT author,name FROM books")
        result = cursor.fetchall()
        for i in result:
            books.append(i)
        return books


def get_user():
    """ мб пригодится, в любом случае тренировочка """

    # todo: просто селект. результат - ну хз. пусть будет Юзернейм
    pass


def user_exists():
    """ проверка, что такой юзверь есть в БД"""

    # todo: метод sql exists. результат - True или False
    pass


def get_book():
    # todo: селект. результат - вся инфа о книге
    pass

