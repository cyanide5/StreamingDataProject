from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy_serializer import SerializerMixin


Base = declarative_base()


class Netflix(Base, SerializerMixin):
    __tablename__ = 'netflix_titles'

    serialize_rules = ('-show_id',)

    show_id = Column(String(50), primary_key=True)
    title = Column(String(50))
    type = Column(String(50))
    director = Column(String(500))
    actors = Column(String(500))
    country = Column(String(500))
    date_added = Column(String(50))
    release_year = Column(String(50))
    rating = Column(String(50))
    duration = Column(String(50))
    listed_in = Column(String(500))
    description = Column(String(500))

