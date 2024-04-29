#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query to list all cities along with their states
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Execute SQL query
    cursor.execute(query)

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()
