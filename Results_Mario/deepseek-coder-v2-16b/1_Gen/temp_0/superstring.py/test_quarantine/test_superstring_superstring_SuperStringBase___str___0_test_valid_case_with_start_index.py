
import pytest
from superstring.superstring import SuperStringBase

@pytest.fixture
def obj():
    return SuperStringBase('Hello', 'World!')

def test_valid_case_with_start_index(obj):
    assert str(obj) == "HelloWorld!"
    assert obj.to_printable() == "HelloWorld!"
    assert obj.to_printable(start_index=6) == "World!"
    assert obj.to_printable(end_index=5) == "Hello"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_start_index.py E [100%]

==================================== ERRORS ====================================
______________ ERROR at setup of test_valid_case_with_start_index ______________

    @pytest.fixture
    def obj():
>       return SuperStringBase('Hello', 'World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_start_index.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_start_index.py::test_valid_case_with_start_index
=============================== 1 error in 0.07s ===============================
"""