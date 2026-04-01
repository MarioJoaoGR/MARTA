
import pytest
from superstring.superstring import SuperStringBase

def test_error_case_invalid_index():
    obj = SuperStringBase()
    
    # Test when start_index is greater than end_index
    with pytest.raises(ValueError):
        obj.to_printable(end_index=2, start_index=5)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_error_case_invalid_index.py F [100%]

=================================== FAILURES ===================================
________________________ test_error_case_invalid_index _________________________

    def test_error_case_invalid_index():
        obj = SuperStringBase()
    
        # Test when start_index is greater than end_index
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_error_case_invalid_index.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_to_printable_0_test_error_case_invalid_index.py::test_error_case_invalid_index
============================== 1 failed in 0.04s ===============================
"""