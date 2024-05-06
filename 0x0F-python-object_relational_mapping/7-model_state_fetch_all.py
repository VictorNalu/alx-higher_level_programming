#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        )
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects and sort by state id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
