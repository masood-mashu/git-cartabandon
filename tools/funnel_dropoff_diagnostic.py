"""
funnel_dropoff_diagnostic.py - Identifies exact checkout stage responsible for transaction abandonment
"""
import sys
import json


def diagnose_funnel_dropoff(checkout_step: str):
    step = checkout_step.lower()
    if "ship" in step:
        issue = "SHIPPING_FEE_SHOCK"
    elif "pay" in step:
        issue = "PAYMENT_GATEWAY_FRICTION"
    else:
        issue = "GENERAL_HESITATION"
    return {"primary_issue": issue, "status": f"{issue}_FLAGGED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "funnel-dropoff-diagnostic"}))
