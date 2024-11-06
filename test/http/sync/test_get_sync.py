import os

from allquests.http.methods import Methods
from allquests.http.proxy import Proxy
from allquests.http.request_args import RequestArgs
from allquests.http.sync.get import get

proxy: Proxy | None = None

if os.environ.get("http_proxy") or os.environ.get("https_proxy"):
    proxy = Proxy("localhost", 3128)

params: RequestArgs = RequestArgs(
    Methods.GET,
    "/api/v2/pokemon/ditto",
    host="pokeapi.co",
    proxy=proxy if proxy else None,
)


def test_get_sync_request():
    res = get(params)
    if res.status != 200:
        msg = f"The request don't complete succesfull. Response get:{res.status}."
        raise RuntimeError(msg)
