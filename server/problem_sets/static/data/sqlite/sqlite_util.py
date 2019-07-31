#  Copyright (c) 2019 Thomas Howe

import os
import sqlite3

from typing import Optional


def sqlite_touch(file: str) -> None:
    """ create a database connection to an SQLite database """
    conn = conn(file)
    if conn:
        print(f"Loaded database at {file.split(os.sep)[-1]}, {sqlite3.version}")
    else:
        print("Failed to load database")

    conn.close()


def connection(file: str) -> Optional[sqlite3.Connection]:
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(file)
        return conn
    except sqlite3.Error as e:
        print(f"SQLITE ERROR: {e}")

    return None


def write_commit(conn: sqlite3.Connection, sql: str, *params):
    try:
        conn.cursor().execute(sql, *params)
        conn.commit()

    except sqlite3.Error as e:
        print(e)


def query_fetch(conn: sqlite3.Connection, sql: str, *params):
    try:
        cursor = conn.cursor()
        cursor.execute(sql, *params)
        return cursor.fetchall()

    except sqlite3.Error as e:
        print(e)