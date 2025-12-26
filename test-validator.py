from signals.parser import parse_signal
from signals.validator import validate_signal

signal_text = """
Gold buy limit 4468-64
SL 4462
TP 4471-75-80
"""

signal = parse_signal(signal_text)
validate_signal(signal)

print("✅ Signal validated successfully")
