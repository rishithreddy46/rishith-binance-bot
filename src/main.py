# src/main.py

from utils import get_client
from logger import logger
from binance.enums import *
from advanced.oco import place_oco_order
from advanced.twap import place_twap_order

def market_order():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    quantity = float(input("Quantity: "))

    client = get_client()
    order = client.futures_create_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )
    logger.info(f"[SIMULATED] Market Order | {symbol} | {side} | Qty: {quantity}")
    print("✅ Market order simulated.")
    print(order)

def limit_order():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    quantity = float(input("Quantity: "))
    price = float(input("Limit Price: "))

    client = get_client()
    order = client.futures_create_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=price
    )
    logger.info(f"[SIMULATED] Limit Order | {symbol} | {side} | Qty: {quantity} | Price: {price}")
    print("✅ Limit order simulated.")
    print(order)

def oco_order():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (SELL only for now): ").upper()
    quantity = float(input("Quantity: "))
    take_profit_price = float(input("Take-Profit Price: "))
    stop_loss_price = float(input("Stop-Loss Trigger Price: "))
    stop_limit_price = stop_loss_price  # For simulation

    place_oco_order(
        symbol=symbol,
        side=SIDE_SELL if side == "SELL" else SIDE_BUY,
        quantity=quantity,
        take_profit_price=take_profit_price,
        stop_loss_price=stop_loss_price,
        stop_limit_price=stop_limit_price
    )

def twap_order():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    total_quantity = float(input("Total Quantity: "))
    slices = int(input("Number of slices (e.g. 5): "))
    interval_sec = int(input("Interval between orders (in seconds): "))

    place_twap_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        total_quantity=total_quantity,
        slices=slices,
        interval_sec=interval_sec
    )

def main():
    while True:
        print("\n📊 BINANCE MOCK TRADING BOT MENU")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. OCO Order")
        print("4. TWAP Order")
        print("5. Exit")

        choice = input("Select an option (1–5): ")

        if choice == '1':
            market_order()
        elif choice == '2':
            limit_order()
        elif choice == '3':
            oco_order()
        elif choice == '4':
            twap_order()
        elif choice == '5':
            print("👋 Exiting bot.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
