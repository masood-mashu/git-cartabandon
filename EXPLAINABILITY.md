# Explainability, Auditability & Decision Logic: GitCartAbandon

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitCartAbandon**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitCartAbandon** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **E-commerce**: E-commerce checkout funnel telemetry (Shopify, WooCommerce, Magento).
- **Product**: Product bill-of-materials margin matrices and real-time shipping rate APIs.
- **Customer**: Customer engagement history and omnichannel messaging consent records.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **diagnose_funnel_dropoff**: Uses `funnel-dropoff-diagnostic` to calculate identifies exact checkout stage responsible for transaction abandonment.
   - **calculate_margin_discount**: Uses `exit-intent-discount-engine` to calculate calculates safe promotional discount that maintains minimum required gross margin.
   - **schedule_recovery_sequence**: Uses `cart-recovery-scheduler` to calculate schedules multi-stage cart recovery notification cadence across email and sms.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an abandoned cart event is detected, the agent runs funnel_dropoff_diagnostic, exit_intent_discount_engine, and cart_recovery_scheduler. If margin permits and customer is eligible, it issues APPROVED. If customer has already received recovery codes in past 30 days, it issues NEEDS_REVIEW. If discount would create negative contribution margin, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on margin mathematical limits.
- **Requires**: Requires real-time inventory reservation holds (expires after 24 hours).
- **Complies**: Complies with FTC truth-in-advertising guidelines for promotional offers.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
