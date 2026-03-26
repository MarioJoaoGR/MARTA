
import pytest
from superstring.superstring import SuperStringBase, SuperStringUpper

@pytest.fixture(scope="module")
def s():
    return SuperStringUpper(SuperStringBase("Hello, World!"))

def test_edge_case(s):
    assert s.to_printable() == "HELLO, WORLD!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_______________________ ERROR at setup of test_edge_case _______________________

    @pytest.fixture(scope="module")
    def s():
>       return SuperStringUpper(SuperStringBase("Hello, World!"))
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_edge_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_edge_case.py::test_edge_case
=============================== 1 error in 0.04s ===============================
"""