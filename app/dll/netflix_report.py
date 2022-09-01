from sqlalchemy import asc, desc

from db import Session
from models import Netflix

session = Session()


def get_report_data(sort_column, sort_dir, page_length, start, filter_by):
    if filter_by:
        query = session.query(Netflix)
    query = session.query(Netflix)
    sort = asc(sort_column) if sort_dir == 'asc' else desc(sort_column)
    sorted_query = query.order_by(sort)
    count = query.count()
    paginated_query = sorted_query.limit(page_length).offset(start)
    resp = [row.to_dict() for row in paginated_query]

    return resp

