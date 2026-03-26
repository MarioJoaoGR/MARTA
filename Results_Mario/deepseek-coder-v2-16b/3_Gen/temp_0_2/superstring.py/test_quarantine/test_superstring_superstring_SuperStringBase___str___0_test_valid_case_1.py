
import pytest
from superstring.superstring import SuperStringBase, SuperStringConcatenation

@pytest.fixture
def setup():
    s1 = SuperStringBase('Hello')
    s2 = SuperStringBase(', World!')
    concat_str = SuperStringConcatenation(s1, s2)
    return concat_str

def test_valid_case_1(setup):
    assert str(setup) == "Hello, World!"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_1.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_case_1 ______________________

    @pytest.fixture
    def setup():
>       s1 = SuperStringBase('Hello')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_1.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_1.py::test_valid_case_1
=============================== 1 error in 0.04s ===============================
"""