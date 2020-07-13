import aiohttp_cors
from aiohttp import web
from views import index

default_config = {
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
}
app = web.Application()
cors = aiohttp_cors.setup(app, defaults=default_config)
cors.add(app.router.add_route("GET", "/", index), default_config)
web.run_app(app, host='127.0.0.1', port=8081)
