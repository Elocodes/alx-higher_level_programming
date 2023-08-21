#!/usr/bin/python3

"""
script lists all "states" whose name match with argument passed.
Script must be safe from sql injection by ensuring that the argument string
passed matches strictly with argument in table. note that column 0 is id.
The module "MySQLdb" id used to connect to the MySQL server.
result is soretd in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    for row_column in cur.fetchall():
        if row_column[1] == args[4]:
            print(row_column)
