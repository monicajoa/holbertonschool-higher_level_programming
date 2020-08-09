#!/usr/bin/python3
""" All cities by state
    cript that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    new_query = "SELECT cities.name"
    new_query += " FROM cities LEFT JOIN states ON cities.state_id=states.id"
    new_query += " WHERE states.name LIKE BINARY %s"
    cur.execute(new_query, (argv[4], ))
    rows = cur.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
    new_str = ', '.join(new_list)
    print(new_str)
    cur.close()
    db.close()
