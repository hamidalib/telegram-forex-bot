from signals.parser import parse_signal
from signals.validator import validate_signal
from trading.engine import can_execute_trade, add_open_trade, list_open_trades

signal_text = """
Gold buy limit 4468-64
SL 4462
TP 4471-75-80
"""

# Parse and validate
signal = parse_signal(signal_text)
validate_signal(signal)

# Check if trade can execute
if can_execute_trade(signal):
    add_open_trade(signal)

list_open_trades()
