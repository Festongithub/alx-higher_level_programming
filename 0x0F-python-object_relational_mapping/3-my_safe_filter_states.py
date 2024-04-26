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
    cur.execute("SELECT * FROM states WHERE BINARY name=%s", [argv[4]])
    # get all states
    states = cur.fetchall()
    # print all states
    for i in states:
        print(i)
        # clean up
        cur.close()
