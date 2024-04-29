#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
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

    # Prepare SQL query with user input using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute SQL query with user input
    cursor.execute(query, (sys.argv[4],))

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
