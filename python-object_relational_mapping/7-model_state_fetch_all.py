#!/usr/bin/python3
# Importing the sql alchemy To interract with the DB
# Impor the sys Module to use the argument
# Import the sessionmaker to make a new session
# Import the State Module to get the class Attributes
"""
This script lists all the state's Objects Ordered by state is
and take the username, the Password and the DB as an argument
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if len(sys.argv) < 4:
    sys.exit(1)

U = sys.argv[1]
Db = sys.argv[3]

if __name__ == "__main__":
    engine = \
     create_engine(f"mysql+mysqldb://{U}:@localhost/{Db}", pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
