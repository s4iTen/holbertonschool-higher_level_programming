#!/usr/bin/python3
"""This is the modules"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(len(sys.argv))
        sys.exit(1)

    conne = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password='',
        db=sys.argv[3]
        )
    curs = conne.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    conne.close()
