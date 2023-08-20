#!/usr/bin/python3

"""
script lists all "states" with a name starting with N. The module "MySQLdb"
id used to connect to the MySQL server. result is soretd in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for items in cur.fetchall():
        print(items)
