
import pytest
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern
import re

def test_invalid_input():
    with pytest.raises(InvalidPattern) as exc_info:
        lazy_regex = LazyRegex()
    assert isinstance(exc_info.value, InvalidPattern), "Expected InvalidPattern but got a different exception"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(InvalidPattern) as exc_info:
E       Failed: DID NOT RAISE <class 'pytutils.lazy.lazy_regex.InvalidPattern'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""