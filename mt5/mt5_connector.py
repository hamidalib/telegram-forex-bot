from typing import Dict
from trading.engine import calculate_risk, add_open_trade
from signals.validator import validate_signal

# Simulation balance (reuse from engine)
ACCOUNT_BALANCE = 100.0
LOT_SIZE = 0.01
MAX_RISK_PERCENT = 3.0
MAX_OPEN_TRADES = 3

# Simulated open trades
open_trades = []


def simulate_trade(signal_text: str):
    """
    Simulate executing a trade:
    - Parse & validate
    - Calculate risk %
    - Check max open trades
    - Print trade details
    """
    try:
        # Parse & validate
        from signals.parser import parse_signal
        signal = parse_signal(signal_text)
        validate_signal(signal)
    except ValueError as e:
        print(f"❌ Signal skipped: {e}")
        return False

    # Check max open trades
    if len(open_trades) >= MAX_OPEN_TRADES:
        print("❌ Max open trades reached. Trade skipped.")
        return False

    # Risk calculation
    entry_price = signal["entry"][0]
    sl_price = signal["sl"]
    risk_percent = calculate_risk(entry_price, sl_price)

    if risk_percent > MAX_RISK_PERCENT:
        print(f"❌ Risk too high ({risk_percent:.2f}%). Trade skipped.")
        return False

    # Simulate trade execution
    print("✅ Trade simulated!")
    print(f"Symbol: {signal['symbol']}")
    print(f"Order Type: {signal['order_type']}")
    print(f"Entry: {signal['entry']}")
    print(f"SL: {signal['sl']}")
    print(f"TP: {signal['tp']}")
    print(f"Estimated Risk: {risk_percent:.2f}%")
    print(f"Lot Size: {LOT_SIZE}")

    # Add to simulated open trades
    open_trades.append(signal)
    return True


def list_simulated_trades():
    """Print all simulated open trades"""
    if not open_trades:
        print("No simulated trades currently.")
        return
    print("\n=== Simulated open trades ===")
    for idx, t in enumerate(open_trades, 1):
        print(f"{idx}. {t['symbol']} {t['order_type']} Entry:{t['entry']} SL:{t['sl']} TP:{t['tp']}")
