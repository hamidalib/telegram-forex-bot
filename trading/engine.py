from typing import Dict, List

# Simulation / configuration
ACCOUNT_BALANCE = 100.0   # USD
MAX_RISK_PERCENT = 3.0    # % per trade
MAX_OPEN_TRADES = 3
LOT_SIZE = 0.01            # fixed lot size

# Keep track of open trades
open_trades: List[Dict] = []


def calculate_risk(entry: float, sl: float, lot: float = LOT_SIZE) -> float:
    """
    Estimate % risk for a trade based on entry, SL, lot size, and account balance.
    For XAUUSD, assume 1 pip = $0.1 per 0.01 lot (simplified)
    """
    pip_distance = abs(entry - sl)
    # Risk per 0.01 lot in USD
    risk_per_lot = pip_distance * 0.1
    # % risk of account
    risk_percent = (risk_per_lot / ACCOUNT_BALANCE) * 100
    return risk_percent


def can_execute_trade(signal: Dict) -> bool:
    """
    Determine if trade can be executed based on max open trades and risk.
    """
    if len(open_trades) >= MAX_OPEN_TRADES:
        print("❌ Max open trades reached. Skipping trade.")
        return False

    # Use the first entry price for risk calculation
    entry_price = signal["entry"][0]
    sl_price = signal["sl"]
    risk_percent = calculate_risk(entry_price, sl_price)

    if risk_percent > MAX_RISK_PERCENT:
        print(f"❌ Trade risk {risk_percent:.2f}% exceeds max {MAX_RISK_PERCENT}%. Skipping trade.")
        return False

    print(f"✅ Trade ready. Estimated risk: {risk_percent:.2f}%")
    return True


def add_open_trade(signal: Dict):
    """
    Add trade to open_trades (simulation)
    """
    open_trades.append(signal)


def list_open_trades():
    """
    Print currently open trades
    """
    if not open_trades:
        print("No open trades currently.")
        return
    print("Current open trades:")
    for idx, t in enumerate(open_trades, 1):
        print(f"{idx}. {t['symbol']} {t['order_type']} Entry:{t['entry']} SL:{t['sl']} TP:{t['tp']}")
