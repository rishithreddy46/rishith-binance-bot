# src/limit_orders.py

import sys
from binance.enums import *
from utils import get_client
from logger import logger

def place_limit_order(symbol, side, quantity, price):
    client = get_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        logger.info(f"[SIMULATED] Limit Order Placed | {symbol} | {side} | Qty: {quantity} | Price: {price}")
        print("✅ Simulated limit order placed.")
        print(order)
    except Exception as e:
        logger.error(f"❌ Failed to simulate limit order: {e}")
        print("❌ Error placing limit order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL BUY/SELL QUANTITY PRICE")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])
    price = float(sys.argv[4])

    if side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Use BUY or SELL.")
        sys.exit(1)

    place_limit_order(symbol, side, quantity, price)
