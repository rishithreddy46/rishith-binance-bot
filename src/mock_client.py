class MockBinanceClient:
    def futures_create_order(self, symbol, side, type, quantity, price=None, timeInForce=None, stopPrice=None):
        if type == "STOP_MARKET":
            print(f"[SIMULATION] {type} (Stop @ {stopPrice}) {side} {quantity} {symbol}")
        else:
            print(f"[SIMULATION] {type} order: {side} {quantity} {symbol} @ {price if price else 'MARKET'}")

        return {
            "orderId": 999999,
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": quantity,
            "price": price,
            "stopPrice": stopPrice,
            "status": "NEW"
        }
