#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one that is
safe from MySQL injections!
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

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id", (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
