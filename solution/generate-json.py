"""
Generar archivo de casos de prueba para ejercicio de verificar número.
"""

import json
from pathlib import Path

PROG_FILE = "validar_numero.py"
YES_REGEX = r"(?i)^(?=.*\b(s[íi]|True)\b)(?!.*\b(no|False)\b).*"
NO_REGEX = r"(?i)^(?!.*\b(s[íi]|True)\b)(?=.*\b(no|False)\b).*"

base_dir = Path(".")
tests_file = base_dir / "solution" / "test_cases.json"


cases_true = [
    "123", "123.456", "-123.456", "+123.456",
    ".123", "+.123", "-.123", ".123+", ".123-",
    "123.", "+123.", "-123.", "123.+", "123.-",
    ".", "-.", ".+",
]
cases_false = [
    "123 ", "abc", "1a23", "-123-", "+123-", "-1-2", "1.2.3",
]
cases = [(case, True) for case in cases_true]
cases += [(case, False) for case in cases_false]

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    inp, outp = case
    if outp:
        outp = YES_REGEX
    else:
        outp = NO_REGEX
    name = f"Test{i:02d}: {inp}"
    entry = {
        "name": name,
        "type": "io",
        "run": "python3 " + PROG_FILE,
        "points": 1,
        "comparison": "regex",
        "input": inp,
        "expected": outp,
        }
    tests.append(entry)

# Añadir sangrías extra para copiar en archivo de Classroom 50
clsrm50 = {"assignments": [{"tests": tests}]}

with tests_file.open("w", encoding="utf-8") as f:
    json.dump(clsrm50, f, indent=2, ensure_ascii=False)
