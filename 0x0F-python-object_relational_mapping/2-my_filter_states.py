#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided

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

    # Prepare SQL query with user input

    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"""
    query = query.format(sys.argv[4])

    # Execute SQL query with user input
    cursor.execute(query)

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
