
import pytest
from superstring.superstring import SuperString, SuperStringBase, SuperStringConcatenation

def test_invalid_input_error_handling():
    s1 = SuperString('Hello')
    right = 123
    
    with pytest.raises(TypeError):
        result = s1.__add__(right)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___2_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        s1 = SuperString('Hello')
        right = 123
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___2_test_invalid_input_error_handling.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___2_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.05s ===============================
"""