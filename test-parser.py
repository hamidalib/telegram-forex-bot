from signals.parser import parse_signal

signal_text = """
Gold buy limit 4468-64
SL 4462
TP 4471-75-80
"""

parsed = parse_signal(signal_text)
print(parsed)
