"""
Generar autograding.json para ejercicio de verificar número.
"""

import json
import random

FILENAME = ".github/classroom/autograding.json"
PROG_FILE = "validar_numero.py"

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
        outp = "^(?=.*(sí |si |True))(?!.*(no |False)).*"
    else:
        outp = "^(?!.*(sí |si |True))(?=.*(no |False)).*"
    name = f"Test{i:02d}: {inp}"
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 1m python " + PROG_FILE,
        "input": inp,
        "output": outp,
        "comparison": "regex",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
