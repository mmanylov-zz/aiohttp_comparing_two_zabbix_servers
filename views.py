from aiohttp import web, ClientSession
from aiohttp.web import Request, Response

from zabbix import get_zabbix_clients


def json_service(handler):
    async def wrapper(request: Request, *args, **kwargs):
        request_data = await request.json()
        response_data = await handler(request_data)
        return web.json_response(response_data)
    return wrapper


@json_service
async def index(request_data: dict):
        query = request_data.get('query')
        clients = await get_zabbix_clients()
        for client in clients:
            hosts = await client.get_hosts()
        return hosts
