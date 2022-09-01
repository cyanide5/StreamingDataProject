import sqlalchemy.exc
from sqlalchemy import func

from db import Session
from models import Netflix
from flask_restx import abort

session = Session()


def get_details(title):
    query = (
        session.query(Netflix)
        .filter(func.lower(Netflix.title).contains(func.lower(title)))
        .limit(100)  # this could be expanded to show more, or less, results as needed (intake from payload?)
    )
    result = query.all()  # .first()

    if not result:
        abort(400, 'No titles found')

    # resp = {
    #     'title': title,
    #     'actors': result.actors,
    #     'type': result.type,
    #     'director': result.director,
    #     'rating': result.rating,
    #     'category': result.listed_in,
    #     'description': result.description,
    #     'release_year': result.release_year,
    #     'duration': result.duration,
    # }
    resp = [row.to_dict() for row in result]
    return resp


def insert_new_title(obj):
    try:
        session.add(
            Netflix(
                show_id='',
                title=obj['title'],
                type=obj['type'],
                director=obj['director'],
                actors=obj['actors'],
                country=['country'],
                date_added='',
                release_year=obj['release_year'],
                rating=obj['rating'],
                duration=obj['duration'],
                listed_in=obj['listed_in'],
                description=obj['description'],
            )
        )

    except Exception():
        # no specific exception, this is only to be viewed as an example as it will likely never be triggered.
        session.rollback()
        abort(
            500,
            f'Unable to add {obj["title"]}',
        )

    session.commit()

    return
