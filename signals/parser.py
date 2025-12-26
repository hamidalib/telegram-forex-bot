import re
from typing import Dict, List


def parse_signal(text: str) -> Dict:
    """
    Parse a forex signal message into structured data.
    Returns a dict if successful, raises ValueError if parsing fails.
    """

    if not text:
        raise ValueError("Empty message")

    text = text.lower()

    # ───────── SYMBOL ─────────
    if "gold" in text or "xau" in text:
        symbol = "XAUUSD"
    else:
        raise ValueError("Unsupported symbol")

    # ───────── DIRECTION ─────────
    if "buy limit" in text:
        order_type = "BUY_LIMIT"
    elif "sell limit" in text:
        order_type = "SELL_LIMIT"
    elif "buy" in text:
        order_type = "BUY"
    elif "sell" in text:
        order_type = "SELL"
    else:
        raise ValueError("Direction not found")

    # ───────── ENTRY PRICE ─────────
    entry_match = re.search(r"(\d{3,5})\s*-\s*(\d{2,5})", text)
    if entry_match:
        high = float(entry_match.group(1))
        low_part = entry_match.group(2)

        # Handle 4468-64 → 4464
        if len(low_part) < len(entry_match.group(1)):
            low = float(entry_match.group(1)[:-len(low_part)] + low_part)
        else:
            low = float(low_part)

        entry = [high, low]
    else:
        entry_single = re.search(r"\b(\d{3,5})\b", text)
        if entry_single:
            entry = [float(entry_single.group(1))]
        else:
            raise ValueError("Entry price not found")

    # ───────── STOP LOSS ─────────
    sl_match = re.search(r"sl\s*(\d{3,5})", text)
    if not sl_match:
        raise ValueError("SL not found")
    sl = float(sl_match.group(1))

    # ───────── TAKE PROFIT ─────────
    tp_match = re.search(r"tp\s*([\d\-]+)", text)
    if not tp_match:
        raise ValueError("TP not found")

    tp_values = tp_match.group(1).split("-")
    tp = [float(v) for v in tp_values if v.isdigit()]

    return {
        "symbol": symbol,
        "order_type": order_type,
        "entry": entry,
        "sl": sl,
        "tp": tp
    }
