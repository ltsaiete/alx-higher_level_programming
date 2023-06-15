#!/usr/bin/python3
"""
This is a simple module and it
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
