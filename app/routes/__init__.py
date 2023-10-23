from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import process
from . import points