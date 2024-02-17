#!/usr/bin/python3

"""script that lists all states from the
database hbtn_0e_usa

Usage:
    ./0-select_states.py <username> <passowrd> <database name>
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    user, pwd, db = sys.argv[1:]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
