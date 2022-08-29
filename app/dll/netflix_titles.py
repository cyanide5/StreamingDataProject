from db import Session
from models import Netflix

session = Session()


def get_details(title):
    query = session.query(Netflix).filter(Netflix.title == title)

    result = query.one()
    resp = {'title': title,
            'actors': result.actors,
            'type': result.type,
            'director': result.director,
            'rating': result.rating,
            'category': result.listed_in,
            'description': result.description,
            'release_year': result.release_year,
            'duration': result.duration}

    return resp


def insert_new_title(obj):
    try:
        session.add(Netflix(show_id='', title=obj['title'], type=obj['type'],
                            director=obj['director'], actors=obj['actors'],
                            country=['country'], date_added='',
                            release_year=obj['release_year'], rating=obj['rating'],
                            duration=obj['duration'], listed_in=obj['listed_in'],
                            description=obj['description']))

    except Exception():
        session.rollback()

    session.commit()

    return





