#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connect to MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database)
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all City objects and sort by city id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        state_name = session.query(State).filter(State.id == city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
