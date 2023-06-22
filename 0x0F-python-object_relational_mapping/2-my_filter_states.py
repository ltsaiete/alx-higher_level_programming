#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
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

    cur.execute(f"SELECT * FROM states WHERE name = {sys.argv[4]} ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
