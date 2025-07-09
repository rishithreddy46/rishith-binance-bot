# src/advanced/twap.py

import time
from utils import get_client
from logger import logger
from binance.enums import *

def place_twap_order(symbol, side, total_quantity, slices, interval_sec):
    client = get_client()
    slice_qty = round(total_quantity / slices, 6)  # avoid float errors

    logger.info(f"[SIMULATED][TWAP] Starting TWAP: {slices} slices of {slice_qty} {symbol} every {interval_sec} sec")

    for i in range(slices):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=slice_qty
            )
            logger.info(f"[SIMULATED][TWAP] Slice {i+1}/{slices}: {order}")
            print(f"✅ Order {i+1}/{slices} placed: {order}")
        except Exception as e:
            logger.error(f"[TWAP ERROR] Slice {i+1}: {e}")
            print(f"❌ TWAP slice failed: {e}")

        if i < slices - 1:
            time.sleep(interval_sec)

    print("✅ TWAP simulation complete.")
