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
        state = sys.argv[4]
        conne = MySQLdb.connect(host=h, user=u, password='', db=sys.argv[3])
        curs = conne.cursor()
        curs.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
        rows = curs.fetchall()
        result = []
        for row in rows:
            if row[4] == sys.argv[4]:
                result.append(row[2])
            else:
                print()
        for i, j in enumerate(result):
            if(i < len(result) - 1):
                print(j, end=", ")
            else:
                print(j)
        curs.close()
        conne.close()
    except Exception as e:
        print(e)
