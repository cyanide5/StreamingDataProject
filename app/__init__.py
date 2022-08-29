from flask import Flask, Blueprint
import logging
from flask_restx import Api
from flask_restx.apidoc import apidoc

from app.apis_v1.netflix import api as netflix_v1
from app.apis_v1.agg import api as agg_v1
from app.apis_v1.hulu import api as hulu_v1

__version__ = '1.0.0'

from connect import connect_with_connector

app = Flask(__name__)
logger = logging.getLogger(__name__)

URL_PREFIX = "/xStreamServices"
apidoc.url_prefix = URL_PREFIX
blueprint = Blueprint('api', __name__, url_prefix=URL_PREFIX)

connect_with_connector()

api = Api(
    blueprint,
    title="Video Streaming Microservices",
    version=__version__,
    description=f'Its a service!',
    catch_all_404s=True,
)

app.register_blueprint(blueprint)

api.add_namespace(netflix_v1)
api.add_namespace(hulu_v1)
api.add_namespace(agg_v1)
