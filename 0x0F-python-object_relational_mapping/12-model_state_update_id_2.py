#!/usr/bin/python3
"""Script that changes the name of a State
 object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        )
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with id = 2
    state = session.query(State)\
                   .filter_by(id=2)\
                   .first()

    # Change the name of the State to 'New Mexico'
    if state:
        state.name = 'New Mexico'
        session.commit()
        print("Name of State with id = 2 changed to 'New Mexico'")
    else:
        print("State with id = 2 not found")

    session.close()
