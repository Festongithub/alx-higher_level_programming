#!/usr/bin/python3
"""The module lists all the states"""
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
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nmeSr)
    # get all states
    states = cur.fetchall()
    # print all states
    for i in states:
        print(i)
        # clean up
        cur.close()
