#!/usr/bin/python3
"""This is the modules"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(len(sys.argv))
        sys.exit(1)

    try:
        h = "localhost"
        u = sys.argv[1]
        search = sys.argv[4]
        conne = MySQLdb.connect(host=h, user=u, password='', db=sys.argv[3])
        curs = conne.cursor()
        curs.execute("SELECT * \
                      FROM states WHERE BINARY states.name\
                      = '{}' ORDER BY id ASC".format(search))
        rows = curs.fetchall()
        for row in rows:
            print(row)
        curs.close()
        conne.close()
    except Exception as e:
        print(e)
