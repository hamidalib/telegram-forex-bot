from mt5.mt5_connector import simulate_trade, list_simulated_trades

signals_texts = [
"""
Gold buy limit 4468-64
SL 4462
TP 4471-75-80
""",
"""
Gold sell limit 4485-90
SL 4490
TP 4475-70-65
""",
"""
Gold buy limit 4470-75
SL 4460
TP 4478-4485
""",
"""
Gold buy limit 4450
SL 4400
TP 4460-4470
"""
]

for idx, text in enumerate(signals_texts, 1):
    print(f"\n--- Processing signal #{idx} ---")
    simulate_trade(text)

list_simulated_trades()
