#!/usr/bin/python3
""" This script lists all states with a name starting
with N from the database hbtn_0e_0_usa

Usage:
    ./1-filter_states.py <username> <passowrd> <database name>
"""

import MySQLdb
import sys


if __name__ == '__main__':
    user, pwd, db = sys.argv[1:]
    host, port = 'localhost', 3306

    with MySQLdb.connect(host=host, port=port, user=user, passwd=pwd,
                         db=db) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
            rows = cur.fetchall()
            for row in rows:
                print(row)
