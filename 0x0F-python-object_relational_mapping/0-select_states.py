#!/usr/bin/python3
"""script that lists all states from the
database hbtn_0e_usa"""

import sys
import MySQLdb

user, pwd, db = sys.argv[1:]
host = 'localhost'
port = 3306

conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db)
cur = conn.cursor()


def get_all_states():
    """gets all states in asceding order"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    get_all_states()
    cur.close()
    conn.close()
