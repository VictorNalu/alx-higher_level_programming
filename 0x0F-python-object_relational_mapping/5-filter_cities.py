#!/usr/bin/python3
"""Lists cities of a given state"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )

    # Create a cursor object
    cur = conn.cursor()

    # Prepare SQL query to list all cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute SQL query with user input (state name)
    cur.execute(query, (sys.argv[4],))

    # Fetch all rows from the result set
    cities = cur.fetchall()

    # Print the results separated by commas
    print(", ".join(city[0] for city in cities))

    # Close cursor and database connection
    cur.close()
    conn.close()
