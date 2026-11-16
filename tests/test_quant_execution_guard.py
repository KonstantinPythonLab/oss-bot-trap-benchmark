# -*- coding: utf-8 -*-
import unittest
from src.quant_execution_guard import evaluate_bar_signal_and_leverage

class TestQuantExecutionGuard(unittest.TestCase):
    def test_evaluate_bar_signal_and_leverage(self):
        # Rising
        self.assertEqual(evaluate_bar_signal_and_leverage([10.0, 11.0], 1, 100, 100), 1.5)
        # Falling
        self.assertEqual(evaluate_bar_signal_and_leverage([11.0, 10.0], 1, 100, 100), 0.5)
        # Flat
        self.assertEqual(evaluate_bar_signal_and_leverage([10.0, 10.0], 1, 100, 100), 1.0)
        # Leverage 21 boundary test
        self.assertEqual(evaluate_bar_signal_and_leverage([10.0, 10.0], 1, 2100, 100), 1.0)

if __name__ == '__main__':
    unittest.main()