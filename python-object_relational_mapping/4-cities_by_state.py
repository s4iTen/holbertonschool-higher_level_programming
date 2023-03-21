#!/usr/bin/python3
"""This is the modules"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(len(sys.argv))
        sys.exit(1)

    try:
        h = "localhost"
        u = sys.argv[1]
        conne = MySQLdb.connect(host=h, user=u, password='', db=sys.argv[3])
        curs = conne.cursor()
        curs.execute("SELECT c.id, c.name, s.name\
                    FROM states AS s RIGHT JOIN cities\
                    AS c ON s.id = c.state_id ORDER BY c.state_id ASC")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        curs.close()
        conne.close()
    except Exception as e:
        print(e)
