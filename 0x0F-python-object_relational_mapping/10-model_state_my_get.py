#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        )
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
