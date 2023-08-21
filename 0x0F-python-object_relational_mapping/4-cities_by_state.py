#!/usr/bin/python3

"""
script lists all "cities" from data on a database. The module "MySQLdb"
id used to connect to the MySQL server. result is soretd in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON cities.state_id=states.id")
    for items in cur.fetchall():
        print(items)
