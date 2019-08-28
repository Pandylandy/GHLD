# -*- coding: utf-8 -*-
from enum import Enum


db = "db.db"


DB_STATES = "database.vdb"


class States(Enum):
    S_ADD = "0"
    S_DONE = "1"
    S_ADD_MY = "2"
    S_NONE = "3"

