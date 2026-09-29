"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitCartAbandon.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.funnel_dropoff_diagnostic import *
from tools.exit_intent_discount_engine import *
from tools.cart_recovery_scheduler import *

class TestGitCartAbandonPredictability(unittest.TestCase):
    def test_funnel_dropoff_diagnostic(self):
        res = diagnose_funnel_dropoff("shipping_method_selection")
        self.assertEqual(res["primary_issue"], "SHIPPING_FEE_SHOCK")
        self.assertEqual(res["status"], "SHIPPING_FEE_SHOCK_FLAGGED")

    def test_exit_intent_discount_engine(self):
        res = calculate_margin_discount('{"retail_price_usd": 100.0, "cost_usd": 40.0, "min_margin_pct": 20.0}')
        self.assertGreater(res["authorized_discount_pct"], 0.0)
        self.assertEqual(res["status"], "COUPON_GENERATED")

    def test_cart_recovery_scheduler(self):
        res = schedule_recovery_sequence("cart_abc123")
        self.assertEqual(len(res["sequence"]), 3)
        self.assertEqual(res["status"], "SEQUENCE_SCHEDULED")


if __name__ == "__main__":
    unittest.main()
