from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

database_config = ConfigParser()
database_config.read('database.ini')

# host = database_config['postgres']['host']
# database = database_config['postgres']['database']
# user = database_config['postgres']['user']
# password = database_config['postgres']['password']

host = 'localhost'
database = 'streaming_services'
user = 'streaming_admin'
password = 'password'

DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(engine))
Base = declarative_base(engine)
