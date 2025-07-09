# src/advanced/oco.py

from utils import get_client
from logger import logger
from binance.enums import *

def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price, stop_limit_price):
    client = get_client()

    try:
        # Simulated take-profit (limit) order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=take_profit_price
        )
        logger.info(f"[SIMULATED][OCO] Take-Profit Order | {tp_order}")
        print("✅ Take-Profit order simulated.")

        # Simulated stop-loss (stop-limit) order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_STOP_MARKET,
            stopPrice=stop_loss_price,
            quantity=quantity
        )
        logger.info(f"[SIMULATED][OCO] Stop-Loss Order | {sl_order}")
        print("✅ Stop-Loss order simulated.")

        print("📦 OCO pair simulated. If one is hit, cancel the other (manual in mock).")

    except Exception as e:
        logger.error(f"❌ Failed to simulate OCO: {e}")
        print("❌ Error placing OCO order:", e)
