
import pytest
from superstring.superstring import SuperStringBase

@pytest.fixture
def obj():
    return SuperStringBase()

def test_valid_case_with_start_index(obj):
    # Test case where only start_index is provided
    assert obj.to_printable(2) == "ng"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_case_with_start_index.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_case_with_start_index _______________________

obj = <superstring.superstring.SuperStringBase object at 0x7fc5f3ebbdd0>

    def test_valid_case_with_start_index(obj):
        # Test case where only start_index is provided
>       assert obj.to_printable(2) == "ng"
E       AssertionError: assert None == 'ng'
E        +  where None = to_printable(2)
E        +    where to_printable = <superstring.superstring.SuperStringBase object at 0x7fc5f3ebbdd0>.to_printable

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_case_with_start_index.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_valid_case_with_start_index.py::test_valid_case_with_start_index
============================== 1 failed in 0.04s ===============================
"""