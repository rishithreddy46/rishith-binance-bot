# Binance Futures Trading Bot (Mock Version)

📈 A command-line simulation bot for Binance USDT-M Futures using a mock client.  
Supports core and advanced order types like **Market**, **Limit**, **OCO**, and **TWAP** orders.  
Built for offline development and learning — no API key or real funds required.

---

## 📁 Project Structure

```
rishith_binance_bot/
├── src/
│   ├── main.py                # CLI entry point
│   ├── market_orders.py       # Market order logic
│   ├── limit_orders.py        # Limit order logic
│   ├── mock_client.py         # Offline Binance API simulator
│   ├── utils.py               # Client loader
│   ├── logger.py              # Logging setup
│   └── advanced/
│       ├── oco.py             # Simulated OCO logic
│       └── twap.py            # TWAP order strategy
├── bot.log                    # Structured log file
├── README.md                  # Setup & usage instructions
├── report.pdf                 # Report with screenshots
└── requirements.txt           # Python dependencies
```

---

## 🚀 Features

- ✅ Market Orders (BUY/SELL)
- ✅ Limit Orders with price and quantity
- ✅ OCO Orders: take-profit and stop-loss pair
- ✅ TWAP Orders: split large order into timed chunks
- ✅ Full offline simulation via `mock_client.py`
- ✅ Structured logging (`bot.log`) with timestamps

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/rishithreddy46/rishith-binance-bot.git
cd rishith-binance-bot
```

### 2. Create a Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, install manually:
```bash
pip install python-binance
```

---

## 🧪 Run the Bot (Offline Mode)

```bash
python src\main.py
```

You will see a CLI menu like:

```
📊 BINANCE MOCK TRADING BOT MENU
1. Market Order
2. Limit Order
3. OCO Order
4. TWAP Order
5. Exit
```

---

## 💡 Example Commands (from CLI)

- `Market Order`: Buy 0.01 BTCUSDT at market price  
- `Limit Order`: Sell 0.01 BTCUSDT at 58000  
- `OCO`: Sell with take-profit at 59000 and stop-loss at 57000  
- `TWAP`: Buy 0.1 BTCUSDT in 5 slices every 5 seconds

---

## 🪵 Logging

All order actions and errors are recorded in:

```
bot.log
```

Includes:
- Order type
- Symbol, side, quantity
- Timestamps
- Errors (if any)

---

## 👨‍💻 Developer Mode: Mock Client

This bot runs entirely offline using:

```python
src/mock_client.py
```

No API keys or network connection needed.  
Perfect for testing logic safely.

---


## 📎 Author

**Rishith Reddy**  
GitHub: https://github.com/rishithreddy46

---

## 📝 Notes

- No real orders are placed — this is for educational/demo use only.
- Can be extended to support real Binance Testnet via real API client.

