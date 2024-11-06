import concurrent.futures
from http import client
from http.client import HTTPResponse

from allquests.http.request_args import RequestArgs


def get(params: RequestArgs):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(__get_async, params)
        return future.result()


def __get_async(
    params: RequestArgs,
) -> HTTPResponse:
    res: HTTPResponse
    match params.proxy:
        case params.proxy if params.proxy:
            proxy_server = client.HTTPSConnection(host=params.proxy.HOST, port=params.proxy.PORT)
            proxy_server.set_tunnel(host=params.host, port=params.port)
            proxy_server.request(
                params.methods.value,
                params.endpoint,
                params.body,
                headers={},
            )
            res = proxy_server.getresponse()
        case proxy if not proxy:
            http = client.HTTPSConnection(host=params.host, port=params.port)
            http.request(params.methods.value, params.endpoint, params.body, params.headers)
            res = http.getresponse()
    return res
