import discpy
import unittest
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

class GatewayTests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_payloads(self):
        directPayload = discpy.GatewayPayload(discpy.GatewayOpCode(10), 1)
        jsonPayload = "{\"op\": 10, \"s\": 1, \"t\": null, \"d\": null}"
        jsonedPayload = discpy.GatewayPayload.fromJSON(jsonPayload)

        self.assertEqual(directPayload, jsonedPayload)
        self.assertEqual(directPayload.toJSON(), jsonedPayload.toJSON())
        self.assertEqual(directPayload.toJSON(), jsonPayload)

class HTTPTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        return super().setUp()

    async def test_get_gateway_url(self):
        client = discpy.HTTPClient()
        response = await client.request(discpy.Request(discpy.Method.GET, "gateway/bot", authentication=os.getenv("BOT_TOKEN")))
        await client.close()
        self.assertEqual("wss://gateway.discord.gg", response["url"])

if __name__ == "__main__":
    unittest.main(verbosity=2)