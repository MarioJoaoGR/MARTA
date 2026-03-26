
import pytest
from string_utils.manipulation import roman_decode

def test_invalid_input_type():
    with pytest.raises(TypeError):
        # Test when input is not a string
        roman_decode(123)  # Assuming 123 is an integer, which should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_decode_1_test_invalid_input_type.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_type ____________________________

    def test_invalid_input_type():
        with pytest.raises(TypeError):
            # Test when input is not a string
>           roman_decode(123)  # Assuming 123 is an integer, which should raise TypeError

python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_decode_1_test_invalid_input_type.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:649: in roman_decode
    return __RomanNumbers.decode(input_string)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__RomanNumbers'>, input_string = 123

    @classmethod
    def decode(cls, input_string: str) -> int:
        if not is_full_string(input_string):
>           raise ValueError('Input must be a non empty string')
E           ValueError: Input must be a non empty string

python-string-utils/string_utils/manipulation.py:119: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_decode_1_test_invalid_input_type.py::test_invalid_input_type
============================== 1 failed in 0.03s ===============================
"""