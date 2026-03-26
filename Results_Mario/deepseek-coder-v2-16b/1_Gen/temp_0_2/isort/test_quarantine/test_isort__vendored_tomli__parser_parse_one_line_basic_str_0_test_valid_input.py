
from typing import Tuple
from isort._vendored.tomli._parser import parse_basic_str, Pos

def parse_one_line_basic_str(src: str, pos: Pos) -> Tuple[Pos, str]:
    pos += 1
    return parse_basic_str(src, pos, multiline=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.09s =============================
"""