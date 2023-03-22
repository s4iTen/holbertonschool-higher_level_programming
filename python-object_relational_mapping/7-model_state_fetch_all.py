#!/usr/bin/python3
"""This is the new module that i used sql alchemy in"""
# Importing the sql alchemy To interract with the DB
# Impor the sys Module to use the argument
# Import the sessionmaker to make a new session
# Import the State Module to get the class Attributes
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
