#!/usr/bin/python3
"""The module performs some sql injection on the database"""
import MySQLdb
from sys import argv
# The code cannot be executed
if __name__ == '__main__':
    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # run cursor on the database
    cur = db.cursor()
    # select from the database
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name=%s", [argv[4]])
    # get all states
    cities = cur.fetchall()
    j = []
    # print all states
    for i in cities:
        j.append(i[1])
        print(" ".join(j))
        # clean up
        cur.close()
