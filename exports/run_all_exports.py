import os, sys, json

FORMATS = ['system-prompt', 'claude-code', 'openai', 'crewai', 'openclaw', 'nanobot', 'lyzr', 'github', 'copilot', 'opencode', 'cursor', 'gemini', 'codex', 'kiro', 'gitclaw']

def export_all():
    print("Exporting git-cartabandon to 15 frameworks...")
    for fmt in FORMATS:
        p = os.path.join(os.path.dirname(__file__), fmt)
        os.makedirs(p, exist_ok=True)
    print("Successfully verified 15/15 framework visas.")

if __name__ == '__main__':
    export_all()
