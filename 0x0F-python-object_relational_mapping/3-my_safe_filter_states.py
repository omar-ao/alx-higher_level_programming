#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument

Usage:
    ./3-my_safe_filter_states.py <user> <password> <db name>
"""


import MySQLdb
import sys


if __name__ == '__main__':
    usr, pwd, db, arg = sys.argv[1:]
    host, port = 'localhost', 3306

    conn = MySQLdb.connect(host=host, port=port, user=usr, passwd=pwd, db=db)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"
    cur.execute(query, (arg,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
