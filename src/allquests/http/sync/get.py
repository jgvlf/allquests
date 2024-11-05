from collections.abc import Mapping
from http import client
from http.client import HTTPResponse

from allquests.http.methods import Methods
from allquests.http.proxy import Proxy


def get(
    methods: Methods,
    endpoint: str,
    body: str | None = None,
    headers: Mapping[str, str] = {},
    *,
    host: str,
    port: int | None = None,
    proxy: Proxy | None,
) -> HTTPResponse:
    res: HTTPResponse
    match proxy:
        case proxy if proxy:
            proxy_server = client.HTTPSConnection(host=proxy.HOST, port=proxy.PORT)
            proxy_server.set_tunnel(host=host, port=port)
            proxy_server.request(
                methods.value,
                endpoint,
                body,
                headers={},
            )
            res = proxy_server.getresponse()
        case proxy if not proxy:
            http = client.HTTPSConnection(host=host, port=port)
            http.request(methods.value, endpoint, body, headers)
            res = proxy_server.getresponse()
    return res
