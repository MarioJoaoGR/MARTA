
import pytest
from superstring.superstring import SuperStringLower

def test_valid_input():
    # Create an instance of SuperStringLower with a base string "Hello, World!"
    str_instance = SuperStringLower("Hello, World!")
    
    # Convert the string to lowercase using the lower method
    lower_str_instance = str_instance.lower()
    
    # Assert that the _base attribute of the instance has been converted to lowercase
    assert lower_str_instance._base == "hello, world!"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_lower_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create an instance of SuperStringLower with a base string "Hello, World!"
        str_instance = SuperStringLower("Hello, World!")
    
        # Convert the string to lowercase using the lower method
        lower_str_instance = str_instance.lower()
    
        # Assert that the _base attribute of the instance has been converted to lowercase
>       assert lower_str_instance._base == "hello, world!"
E       AssertionError: assert 'Hello, World!' == 'hello, world!'
E         
E         - hello, world!
E         ? ^      ^
E         + Hello, World!
E         ? ^      ^

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_lower_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_lower_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""