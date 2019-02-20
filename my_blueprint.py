from sanic.response import json, text
from sanic import Blueprint

bp = Blueprint('my_blueprint', url_prefix='/v1')

@bp.route('/blueprint')

async def bp_root(request):
    return json({'my': 'blueprint'})

@bp.middleware

async def print_on_request(request):
    print('i am sa spy')

@bp.middleware('request')

async def print_on_request2(request):
    return text('request')

@bp.middleware('response')

async def print_on_response(request, response):
    return text('response')
