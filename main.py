from sanic import Sanic
from sanic.response import text, json
from sanic.exceptions import ServerError
from sanic.exceptions import NotFound

from controller.index import indexBp

from config import config

app = Sanic(__name__)

app.config.from_object(config)

app.blueprint(indexBp)

app.static('/static', './static')

@app.exception(NotFound)

def ignore_404s(request, exception):
    return text('ddd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)