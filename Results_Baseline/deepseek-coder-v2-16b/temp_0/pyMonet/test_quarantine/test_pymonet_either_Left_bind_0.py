
import pytest
from pymonet.either import Left

# Test initialization with an error message
def test_left_initialization_with_error_message():
    left_instance = Left("An error occurred")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_either_Left_bind_0.py F.              [100%]

=================================== FAILURES ===================================
_________________ test_left_initialization_with_error_message __________________

    def test_left_initialization_with_error_message():
        left_instance = Left("An error occurred")
>       assert str(left_instance) == "An error occurred"
E       AssertionError: assert '<pymonet.eit...7f71dcfa6450>' == 'An error occurred'
E         
E         - An error occurred
E         + <pymonet.either.Left object at 0x7f71dcfa6450>

pyMonet/Test4DT_tests/test_pymonet_either_Left_bind_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Left_bind_0.py::test_left_initialization_with_error_message
========================= 1 failed, 1 passed in 0.05s ==========================
"""