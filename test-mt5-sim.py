from signals.parser import parse_signal
from signals.validator import validate_signal
from mt5.mt5_connector import simulate_trade, list_simulated_trades

signal_text = """
Gold buy limit 4468-64
SL 4462
TP 4471-75-80
"""

# Parse & validate
signal = parse_signal(signal_text)
validate_signal(signal)

# Simulate trade
simulate_trade(signal)

# List open trades
list_simulated_trades()
