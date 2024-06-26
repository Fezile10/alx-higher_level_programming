
#!/usr/bin/python3
"""
    script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).order_by(State.id)
    for i in stmt:
        print("{:d}: {:s}".format(i.id, i.name))
        for j in i.cities:
            print("\t{:d}: {:s}".format(j.id, j.name))
    session.close()
