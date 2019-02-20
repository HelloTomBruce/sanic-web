from sanic.response import json, text
from sanic import Blueprint

from service import index as IndexController

indexBp = Blueprint('index_bp', url_prefix = '/')

@indexBp.route('/getList')

async def getList(request):
    res = IndexController.getList(request)
    return json(res)

