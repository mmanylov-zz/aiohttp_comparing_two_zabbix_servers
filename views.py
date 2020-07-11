from aiohttp import web, ClientSession
from aiohttp.web import Request, Response

from zabbix import get_zabbix_clients


def json_response(handler):
    async def wrapper(*args, **kwargs):
        data = await handler(*args, **kwargs)
        return web.json_response(data)

    return wrapper

@json_response
async def index(request: Request):
    data = await request.json()
    query = data.get('query')
    clients = await get_zabbix_clients()
    for client in clients:
        hosts = await client.get_hosts()
        print(hosts)
        print()
