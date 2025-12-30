from signals.parser import parse_signal

signal_text = """
Gold buy limit 4371-67
SL 4360
TP 4371-4377-4381
(If M1 candle break SL -> exit)

Proper Risk Management is the key to Success in Trading!
"""

parsed = parse_signal(signal_text)
print(parsed)
