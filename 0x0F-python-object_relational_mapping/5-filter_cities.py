#!/usr/bin/python3

"""
script lists all "cities" in a state passed as argument.
script must be sql injection free. The module "MySQLdb"
is used to connect to the MySQL server. result is soretd in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON cities.state_id=states.id")
    city = []
    for row_column in cur.fetchall():
        if row_column[2] == args[4]:
            city.append(row_column[1])
    print(", ".join(city))
