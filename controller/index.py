from sanic.response import json, text
from sanic import Blueprint

from service import index as IndexController

indexBp = Blueprint('index_bp', url_prefix = '/')

@indexBp.route('/getList')

async def getList(request):
    res = IndexController.getList(request)
    return json(res)

@indexBp.route('/getNotice')

async def getNotice(request):
    url = request.args['url'][0]
    encodeType = request.args['encodeType'][0]
    urlType = request.args['type'][0]
    notice = IndexController.getNotice(url, encodeType, urlType)
    res = json(notice)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

