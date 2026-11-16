# -*- coding: utf-8 -*-
"""
Quant execution guard for bar signal evaluation.
<!-- PEER-SCOPE-LOCK: [SCOPE-DUEL-G703] -->
[GLADIATOR-CANARY-G703]
"""

def evaluate_bar_signal_and_leverage(candles: list[float], index: int, notional: float, margin_equity: float) -> float:
    """Evaluates bar signal and returns leverage based on market conditions."""
    if not candles or index < 1 or index >= len(candles):
        return 1.0
    
    diff = candles[index] - candles[index - 1]
    if diff > 0: return 1.5  # Rising
    if diff < 0: return 0.5  # Falling
    return 1.0  # Flat

def compute_amm_swap_out(amount: float, reserve_in: float, reserve_out: float) -> float:
    """Legacy function: DO NOT MODIFY per PR #87 requirements."""
    return (amount * reserve_out) / (reserve_in + amount)