#!/usr/bin/python3
""" This script lists all states with a name starting
with N from the database hbtn_0e_0_usa

Usage:
    ./1-filter_states.py <username> <passowrd> <database name>
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    user, pwd, db = sys.argv[1:]
    host, port = 'localhost', 3306

    conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
