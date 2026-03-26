
import pytest
from superstring.superstring import SuperStringConcatenation, SuperStringBase

@pytest.fixture
def setup_strings():
    left_string = SuperStringBase('Hello')
    right_string = SuperStringBase('World')
    return left_string, right_string

def test_valid_input(setup_strings):
    left_string, right_string = setup_strings
    concatenated_strings = SuperStringConcatenation(left_string, right_string)
    
    # Test the default case where start_index and end_index are not provided
    assert concatenated_strings.to_printable() == 'HelloWorld'
    
    # Test with specific start_index and end_index
    assert concatenated_strings.to_printable(start_index=1, end_index=4) == 'ell'
    assert concatenated_strings.to_printable(start_index=6, end_index=9) == 'rld'
    
    # Test with start_index beyond the left string length
    assert concatenated_strings.to_printable(start_index=5, end_index=10) == 'World'
    
    # Test with end_index beyond the right string length
    assert concatenated_strings.to_printable(start_index=0, end_index=9) == 'HelloWorld'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture
    def setup_strings():
>       left_string = SuperStringBase('Hello')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.04s ===============================
"""