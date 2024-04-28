#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: {} username password database_name state_name"
            .format(sys.argv[0])
        )
        sys.exit(1)

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

    # Prepare SQL query with user input
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute SQL query with user input
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
