
import pytest
from string_utils.manipulation import __RomanNumbers

def test_index_for_sign():
    # Test valid input 'I'
    assert __RomanNumbers.__index_for_sign('I') == 0
    
    # Test valid input 'V'
    assert __RomanNumbers.__index_for_sign('V') == 1
    
    # Test valid input 'X'
    assert __RomanNumbers.__index_for_sign('X') == 2
    
    # Test valid input 'L'
    assert __RomanNumbers.__index_for_sign('L') == 3
    
    # Test valid input 'C'
    assert __RomanNumbers.__index_for_sign('C') == 4
    
    # Test valid input 'D'
    assert __RomanNumbers.__index_for_sign('D') == 5
    
    # Test valid input 'M'
    assert __RomanNumbers.__index_for_sign('M') == 6

def test_invalid_token():
    with pytest.raises(ValueError):
        __RomanNumbers.__index_for_sign('Z')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_index_for_sign ______________________________

    def test_index_for_sign():
        # Test valid input 'I'
>       assert __RomanNumbers.__index_for_sign('I') == 0
E       AttributeError: type object '__RomanNumbers' has no attribute '__index_for_sign'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py:7: AttributeError
______________________________ test_invalid_token ______________________________

    def test_invalid_token():
        with pytest.raises(ValueError):
>           __RomanNumbers.__index_for_sign('Z')
E           AttributeError: type object '__RomanNumbers' has no attribute '__index_for_sign'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py:29: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py::test_index_for_sign
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py::test_invalid_token
============================== 2 failed in 0.04s ===============================
"""