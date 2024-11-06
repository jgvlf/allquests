from collections.abc import Mapping

from allquests.http.methods import Methods
from allquests.http.proxy import Proxy


class RequestArgs:
    def __init__(
        self,
        methods: Methods,
        endpoint: str,
        body: str | None = None,
        headers: Mapping[str, str] = {},
        *,
        host: str,
        port: int | None = None,
        proxy: Proxy | None = None,
    ):
        self.methods: Methods = methods
        self.endpoint: str = endpoint
        self.body: str | None = body
        self.headers: Mapping[str, str] = headers
        self.host: str = host
        self.port: int | None = port
        self.proxy: Proxy | None = proxy
