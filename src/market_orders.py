import sys
from binance.enums import *
from utils import get_client
from logger import logger

def place_market_order(symbol, side, quantity):
    client = get_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logger.info(f"[SIMULATED] Market Order Placed | {symbol} | {side} | Qty: {quantity}")
        print("✅ Simulated market order placed.")
        print(order)
    except Exception as e:
        logger.error(f"❌ Failed to simulate market order: {e}")
        print("❌ Error placing market order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL BUY/SELL QUANTITY")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])

    if side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Use BUY or SELL.")
        sys.exit(1)

    place_market_order(symbol, side, quantity)
