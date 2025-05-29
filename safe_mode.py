import re

risky_patterns = [
    r"(?i)\bignore\b.*\binstruction",
    r"(?i)\bbypass\b.*\bsecurity",
    r"(?i)\bforget\b.*\bprevious",
    r"(?i)\bforget.*instruction",
    r"(?i)\bdisable\b.*\bsafety",
    r"(?i)\bpretend\b.*\bunrestricted",
    r"(?i)\breveal\b.*\binternal.*code",
    r"(?i)\bjailbreak",
    r"(?i)\bhow to\b.*\b(make|prepare).*\bbomb",
    r"(?i)\bprepare\b.*\bbomb",
    r"(?i)\bmake\b.*\bbomb"
]

def is_prompt_risky(prompt):
    return any(re.search(pattern, prompt) for pattern in risky_patterns)
