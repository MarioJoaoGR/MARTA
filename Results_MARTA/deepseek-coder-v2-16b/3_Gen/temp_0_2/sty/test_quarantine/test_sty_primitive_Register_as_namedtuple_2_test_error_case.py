
from sty.primitive import Register
import pytest
from collections import namedtuple

def test_error_case():
    reg = Register()
    result = reg.as_namedtuple()
    assert isinstance(result, namedtuple)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_2_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        reg = Register()
        result = reg.as_namedtuple()
>       assert isinstance(result, namedtuple)
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_2_test_error_case.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_2_test_error_case.py::test_error_case
============================== 1 failed in 0.02s ===============================
"""