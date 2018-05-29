# -*- coding: utf-8 -*-
from bot.config import DB
import sqlite3


with sqlite3.connect(DB) as con:
    con.cursor().execute("CREATE TABLE user(id,name)")
