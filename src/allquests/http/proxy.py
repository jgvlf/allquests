class Proxy:
    def __init__(self, host: str, port: int | None):
        self.HOST: str = host
        self.PORT: int | None = port
