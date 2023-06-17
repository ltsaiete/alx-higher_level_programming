#!/usr/bin/python3
"""
This is a simple module and it only lists
all states from the database hbtn_0e_0_usa
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    HOST = 'localhost'
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
