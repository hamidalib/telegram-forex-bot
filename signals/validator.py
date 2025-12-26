from typing import Dict


def validate_signal(signal: Dict) -> None:
    """
    Validate parsed signal data.
    Raises ValueError if signal is unsafe or invalid.
    """

    order_type = signal["order_type"]
    entry = signal["entry"]
    sl = signal["sl"]
    tp = signal["tp"]

    # ───────── BASIC CHECKS ─────────
    if not tp or len(tp) == 0:
        raise ValueError("No TP levels provided")

    if order_type.startswith("BUY"):
        lowest_entry = min(entry)
        highest_tp = max(tp)

        if sl >= lowest_entry:
            raise ValueError("SL is not below entry for BUY")

        if highest_tp <= lowest_entry:
            raise ValueError("TP is not above entry for BUY")

    elif order_type.startswith("SELL"):
        highest_entry = max(entry)
        lowest_tp = min(tp)

        if sl <= highest_entry:
            raise ValueError("SL is not above entry for SELL")

        if lowest_tp >= highest_entry:
            raise ValueError("TP is not below entry for SELL")

    else:
        raise ValueError("Unknown order type")
