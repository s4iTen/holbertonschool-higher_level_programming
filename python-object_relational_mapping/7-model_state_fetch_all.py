#!/usr/bin/python3
"""
    This script lists all the state's Objects from the database hbtn_0e_6_usa
    Ordered by state isand take the Username,
    the Password and the DB as an arguments
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)

    Us = sys.argv[1]
    Db = sys.argv[3]
    S = "mysql+mysqldb://"
    engine = create_engine(f"{S}{Us}:@localhost/{Db}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
