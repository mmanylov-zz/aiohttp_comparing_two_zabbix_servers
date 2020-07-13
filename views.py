from aiohttp import web
from aiohttp.web import Request

from zabbix import get_zabbix_clients, get_matching_hosts


def json_service(handler):
    async def wrapper(request: Request, *args, **kwargs):
        request_data = await request.json()
        response_data = await handler(request_data)
        return web.json_response(response_data)
    return wrapper


def json_response(handler):
    async def wrapper(request: Request, *args, **kwargs):
        response_data = await handler(request, *args, **kwargs)
        return web.json_response(response_data)
    return wrapper

@json_response
async def index(request):
        clients = await get_zabbix_clients()
        for client in clients:
            client.hosts = await client.get_hosts()

        matching_hosts = await get_matching_hosts(*clients)

        return matching_hosts
