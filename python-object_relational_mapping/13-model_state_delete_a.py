#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, and database name
    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    # Create engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    try:
        # Query all State objects with a name containing the letter 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete all filtered State objects
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
