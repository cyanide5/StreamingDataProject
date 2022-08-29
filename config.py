from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


host = 'localhost'
database = 'streaming_services'
user = 'streaming_admin'
password = 'password'

DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(engine))
Base = declarative_base(engine)
