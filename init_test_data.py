import asyncio

from zabbix import ZabbixClient, ZABBIX_URLS


def get_zabbix_host_create_payload(auth_token, host, interface_ip, req_id):
    return {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": host,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": interface_ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "2"
                }
            ],
            "tags": [
                {
                    "tag": "Host name",
                    "value": "Linux server"
                }
            ]
        },
        "auth": auth_token,
        "id": req_id
    }


def generate_hosts():
    hosts = list()
    return hosts


async def create_hosts():
    for url in ZABBIX_URLS:
        client = ZabbixClient(url)
        await client.authorize()
        await client.call_api(get_zabbix_host_create_payload(client.auth_token, "Ubuntu Server 1", "192.168.3.1", 2))
        await client.call_api(get_zabbix_host_create_payload(client.auth_token, "Ubuntu Server 2", "192.168.3.2", 3))
        await client.call_api(get_zabbix_host_create_payload(client.auth_token, "Ubuntu Server 3", "192.168.3.3", 4))


async def get_host_groups():
    client = ZabbixClient(ZABBIX_URLS[0])
    await client.authorize()
    result = await client.get_host_groups()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(create_hosts())
loop.close()
