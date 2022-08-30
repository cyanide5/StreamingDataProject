import logging

from flask_restx import Namespace, Resource
from app.bll.agg import agg_data

api = Namespace("v1/agg", description="Aggregate Summary Data")


@api.route('/ratings/')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class RatingsAggResource(Resource):
    @api.doc(responses={500: '{column} is not a supported agg type'})
    def get(self):
        return agg_data('rating')
