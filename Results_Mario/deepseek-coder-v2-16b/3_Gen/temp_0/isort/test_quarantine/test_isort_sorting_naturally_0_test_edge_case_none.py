
import re
from typing import Iterable, Callable, Any
from isort.sorting import _natural_keys  # Assuming this is the correct module path

def naturally(
    to_sort: Iterable[str], key: Callable[[str], Any] | None = None, reverse: bool = False
) -> list[str]:
    """Returns a naturally sorted list"""
    if key is None:
        key_callback = _natural_keys
    else:
        def key_callback(text: str) -> list[Any]:
            return _natural_keys(key(text))

    return sorted(to_sort, key=key_callback, reverse=reverse)

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