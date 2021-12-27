import discpy
import unittest

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

if __name__ == "__main__":
    unittest.main(verbosity=2)