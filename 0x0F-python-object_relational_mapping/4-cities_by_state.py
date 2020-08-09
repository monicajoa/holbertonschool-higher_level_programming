#!/usr/bin/python3
""" Cities by states
    script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    new_query = "SELECT cities.id, cities.name, states.name"
    new_query += " FROM cities LEFT JOIN states ON cities.state_id=states.id"
    cur.execute(new_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
