from enum import Enum
from aiohttp import ClientSession

class Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class Request:
    API_BASE_URL = "https://discord.com/api"
    API_VERSION = "v9"

    def __init__(self, method: Method, url: str, *args, **kwargs):
        self.method = method
        self.url = f"{self.API_BASE_URL}/{self.API_VERSION}/{url}"
        self.data = kwargs.get("data", dict())
        self.headers = kwargs.get("headers", dict())
        self.params = kwargs.get("params", dict())
        if kwargs.get("authentication") is not None:
            self.addAuthentication(kwargs.get("authentication"))

    def addAuthentication(self, token: str, bot: bool = True):
        if bot:
            authentication = "Bot"
        else:
            authentication = "Bearer"
        authentication += f" {token}"
        self.headers["Authorization"] = authentication

class HTTPClient:
    def __init__(self):
        self.client = ClientSession()
    
    async def close(self):
        await self.client.close()

    async def request(self, request: Request):
        async with self.client.request(method=request.method.value, url=request.url, data=request.data, headers=request.headers, params=request.params) as request:
            return await request.json()