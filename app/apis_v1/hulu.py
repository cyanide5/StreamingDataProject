import logging
from flask_restx import Namespace, Resource, reqparse
from app.bll.title import title_details

api = Namespace("v1/hulu", description="hulu data")

logger = logging.getLogger(__name__)

parser = reqparse.RequestParser()
parser.add_argument(
    'rating', type=str, required=True, case_sensitive=False, location='form'
)


@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class TitleResource(Resource):
    @api.deprecated
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        details = title_details(args['title'])

        return details

    @api.deprecated
    @api.expect(parser)
    def post(self):
        args = parser.args
        rating = args['rating']
        return


api.add_resource(TitleResource, '/title/details/')
