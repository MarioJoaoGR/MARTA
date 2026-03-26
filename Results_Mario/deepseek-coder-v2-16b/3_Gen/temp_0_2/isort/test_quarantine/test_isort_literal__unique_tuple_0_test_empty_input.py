
from isort.literal import ISortPrettyPrinter
from typing import Any

def _unique_tuple(value: tuple[Any, ...], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(tuple(sorted(set(value))))

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
============================ no tests ran in 0.10s =============================
"""