from flask_restx import abort
from db import Session
from models import Netflix

session = Session()


def data_count(column):

    query = session.query(Netflix)
    if column == 'rating':
        rating_options = ('TV-G', 'TV-PG', 'PG-13', 'TV-MA', 'TV-Y', 'TV-Y7', 'NR')
        rating_count = {}

        for rating in rating_options:
            rating_count[rating] = query.filter_by(rating=rating).count()

        return rating_count

    else:
        abort(500, f'{column} is not a supported agg type')
