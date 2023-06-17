#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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

    cur.execute("""
                SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON cities.state_id=states.id
                ORDER BY cities.id
                """)

    rows = cur.fetchall()
    for row in rows:
        print(row)
