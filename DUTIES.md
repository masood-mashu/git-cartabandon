# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitCartAbandon** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitCartAbandon Automation Engine`
* **Responsibilities**:
  * Analyzes checkout step dropout funnels, computes margin-safe incentive discount codes, and schedules sequences.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitCartAbandon Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies customer coupon eligibility history to prevent repetitive coupon gaming.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `VP of E-Commerce / Growth Marketing Lead (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
