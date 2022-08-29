from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# this was here to connect to my local instance of postgres
# i was originally using a database.ini file
# however, that stopped working and i didn't want to invest time into fixing it

host = 'localhost'
database = 'streaming_services'
user = 'streaming_admin'
password = 'password'

DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(engine))
Base = declarative_base(engine)
