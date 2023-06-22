#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    HOST = 'localhost'
    USER = sys.argv[1]
    PASS = ''  # sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()

    cur.execute("""
                SELECT cities.name FROM cities
                INNER JOIN states ON cities.state_id=states.id
                WHERE states.name = %s
                ORDER BY cities.id
                """, (sys.argv[4],))

    rows = cur.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i != len(rows) - 1:
            print(', ', end="")

    print()
