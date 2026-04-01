
from string_utils.manipulation import roman_encode
import pytest

def test_invalid_type():
    """Test that the function raises a TypeError for inputs other than int or str."""
    with pytest.raises(TypeError) as excinfo:
        roman_encode(None)  # Passing None, which is an invalid type
    assert str(excinfo.value) == "Input must be either an integer or a string representing an integer."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_encode_3_test_invalid_type.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_type _______________________________

    def test_invalid_type():
        """Test that the function raises a TypeError for inputs other than int or str."""
        with pytest.raises(TypeError) as excinfo:
>           roman_encode(None)  # Passing None, which is an invalid type

python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_encode_3_test_invalid_type.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:634: in roman_encode
    return __RomanNumbers.encode(input_number)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__RomanNumbers'>, input_number = None

    @classmethod
    def encode(cls, input_number: Union[str, int]) -> str:
        # force input conversion to a string (we need it in order to iterate on each digit)
        input_string = str(input_number)
    
        if not is_integer(input_string):
>           raise ValueError('Invalid input, only strings or integers are allowed')
E           ValueError: Invalid input, only strings or integers are allowed

python-string-utils/string_utils/manipulation.py:84: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_encode_3_test_invalid_type.py::test_invalid_type
============================== 1 failed in 0.05s ===============================
"""