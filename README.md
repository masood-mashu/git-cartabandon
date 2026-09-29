# GitCartAbandon (`git-cartabandon`)

[![OpenGAP Standard](https://img.shields.io/badge/OpenGAP-v0.1.0-blue.svg)](https://opengap.org)
[![Category](https://img.shields.io/badge/Category-Retail%20%26%20e-commerce-success.svg)](https://hidevs.com)
[![Visas](https://img.shields.io/badge/Visas-15%2F15%20Earned-brightgreen.svg)](#framework-visas)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

**GitCartAbandon** is an OpenGAP-compliant, autonomous autonomous e-commerce cart abandonment diagnostic, margin-preserving recovery agent.

---

## 🏛️ Architecture & OpenGAP Compliance
- `agent.yaml`: Canonical OpenGAP specification manifest.
- `SOUL.md`: Identity, operational boundaries, and audit trail requirements.
- `DUTIES.md`: Explicit separation of duties (Maker vs. Checker vs. Approver).
- `RULES.md`: Zero-tolerance compliance rules and constraints.
- `AGENTS.md`: Multi-agent team workflow and fallback runtime instructions.
- `EXPLAINABILITY.md`: Detailed auditability, decision logic, and boundary documentation.
- `memory/`: Persistent state and session audit logs.
- `tools/`: Deterministic execution tools with strict YAML and JSON Schemas.
- `skills/`: Standardized procedural workflows.
- `exports/`: Multi-framework portability adapters across 15 frameworks.

---

## 🎯 Framework Visas (15 of 15 Frameworks)
Certified portable across System Prompt, Claude Code, OpenAI SDK, CrewAI, OpenClaw, Nanobot, Lyzr, GitHub Copilot, OpenCode, Cursor, Gemini, Codex, Kiro, and GitClaw.

---

## 🧪 Testing & Verification
```bash
python tests/eval_predictability.py
python exports/run_all_exports.py
npx @open-gitagent/opengap validate
```

---

## 📄 License
Apache License 2.0. See [LICENSE](LICENSE) for details.
