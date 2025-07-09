import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "False").lower() == "true"

if USE_MOCK:
    from mock_client import MockBinanceClient
else:
    from binance.client import Client

def get_client():
    if USE_MOCK:
        print("[INFO] Using Mock Binance Client (offline simulation)")
        return MockBinanceClient()
    else:
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        return Client(api_key, api_secret)
