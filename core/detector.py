import re

def is_forex_signal(text: str) -> bool:
    if not text:
        return False

    text = text.lower()

    # ───────── Instrument (Gold / XAU) ─────────
    instrument_pattern = r"\b(gold|xau|xauusd)\b"

    # ───────── Trade Direction ─────────
    direction_pattern = r"\b(buy|sell|buy limit|sell limit)\b"

    # ───────── Stop Loss ─────────
    sl_pattern = r"\bsl\b\s*\d+"

    # ───────── Take Profit ─────────
    tp_pattern = r"\btp\b\s*\d+"

    has_instrument = re.search(instrument_pattern, text)
    has_direction = re.search(direction_pattern, text)
    has_sl = re.search(sl_pattern, text)
    has_tp = re.search(tp_pattern, text)

    return all([has_instrument, has_direction, has_sl, has_tp])
