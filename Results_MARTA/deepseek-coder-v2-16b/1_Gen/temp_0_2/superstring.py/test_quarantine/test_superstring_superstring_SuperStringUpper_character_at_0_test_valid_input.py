
import pytest
from superstring.superstring import SuperStringBase, SuperStringUpper

@pytest.fixture(scope="module")
def base_string():
    return SuperStringBase('Hello, World!')

def test_valid_input(base_string):
    upper_case_extractor = SuperStringUpper(base_string)
    assert upper_case_extractor.character_at(7) == 'W'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture(scope="module")
    def base_string():
>       return SuperStringBase('Hello, World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.04s ===============================
"""