import logging

from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse, abort
from app.bll.title import title_details, add_title, update_title
from app.bll.report import report

# from app.bll.netflix import title_details, add_title, update_title, report

api = Namespace("v1/netflix", description="netflix data")

logger = logging.getLogger(__name__)

title_parser = reqparse.RequestParser()
report_parser = reqparse.RequestParser()

body = api.model('Title', {
    'title': fields.String(example='A Movie Title', required=True),
    'type': fields.String(example='Movie', required=True),
    'director': fields.String(example='Brent Maddock'),
    'actors': fields.String(example='Matt Daemon'),
    'country': fields.String(example='United States'),
    'release_year': fields.String(example='1991', required=True),
    'rating': fields.String(example='TV-G', required=True),
    'duration': fields.String(example='82 min', required=True),
    'listed_in': fields.String(example='Documentaries', required=True),
    'description': fields.String(example='A movie about a person', required=True)
})


@api.route('/title/details/')
@api.response(200, "Title Added")
@api.response(400, "Unsupported request")
class TitleDetailsResource(Resource):
    """
    Searches, Creates, or Updates a given Title details

    get -- returns the details for the provided title
    post -- creates a title
    put -- updates the details for the provided title
    """

    # Search
    title_parser.add_argument('title', type=str, location='args')

    @api.doc('what does this do?')
    @api.expect(title_parser)
    def get(self):
        args = title_parser.parse_args()
        details = title_details(args['title'])
        return details

    @api.expect(body)
    def post(self):
        json_data = request.get_json(force=True)
        add_title(json_data)
        title_result = title_details(json_data['title'])
        if title_result:
            return title_result
        else:
            abort(500, f'There was an error adding the title: {title_result}')

    @api.deprecated
    @api.expect(body)
    def put(self):
        args = title_parser.parse_args()
        json_data = request.get_json(force=True)
        t = update_title(args['title'], json_data)
        return


@api.route('/report/')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class ReportResource(Resource):
    """
    """

    # Sort (assuming front-end report has an anchor column
    report_parser.add_argument('sort_by', type=str, choices=['type', 'title', 'director',
                                                             'actors', 'country', 'release_year', 'rating',
                                                             'duration', 'listed_in'], location='args', required=True)

    report_parser.add_argument('sort_dir', type=str, choices=['asc', 'desc'], location='args', required=True)

    # Pagination (assuming front-end report pagination will start with 0 then increment up as needed)
    report_parser.add_argument('start', type=int, location='args', required=True)
    report_parser.add_argument('page_length', type=int, location='args', required=True)

    # Filter (
    report_parser.add_argument('filter_by', type=str, choices=[], location='args')

    @api.expect(report_parser)
    def get(self):
        args = report_parser.parse_args()
        report_data = report(sort_column=args['sort_by'],
                             sort_dir=args['sort_dir'],
                             page_length=args['page_length'],
                             start=args['start'],
                             filter_by=args['filter_by'])

        return report_data
