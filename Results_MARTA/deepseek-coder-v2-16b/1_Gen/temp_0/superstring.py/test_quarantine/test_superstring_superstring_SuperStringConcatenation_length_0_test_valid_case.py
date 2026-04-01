
import pytest
from superstring.superstring import SuperStringConcatenation

@pytest.fixture
def setup_concatenation():
    left = "Hello"
    right = "World"
    return SuperStringConcatenation(left, right)

def test_valid_case(setup_concatenation):
    ssc = setup_concatenation
    assert ssc.concatenate() == "HelloWorld"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_length_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

setup_concatenation = <superstring.superstring.SuperStringConcatenation object at 0x7fb6be91a3d0>

    def test_valid_case(setup_concatenation):
        ssc = setup_concatenation
>       assert ssc.concatenate() == "HelloWorld"
E       AttributeError: 'SuperStringConcatenation' object has no attribute 'concatenate'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_length_0_test_valid_case.py:13: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_length_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.04s ===============================
"""