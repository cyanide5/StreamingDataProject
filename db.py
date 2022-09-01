from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from authenticate_with_adc import authenticate
from config import DATABASE_URI
from connect import connect_with_connector

authenticate()
engine = connect_with_connector()
Session = sessionmaker(bind=engine)
