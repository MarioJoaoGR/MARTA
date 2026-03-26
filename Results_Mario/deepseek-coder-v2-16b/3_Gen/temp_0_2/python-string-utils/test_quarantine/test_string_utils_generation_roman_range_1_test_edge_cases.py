
import pytest
from string_utils.manipulation import roman_encode
from string_utils.generation import roman_range

def test_edge_cases():
    # Test generating Roman numerals from 1 to 7
    expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    result = list(roman_range(7))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
    # Test generating Roman numerals from 7 down to 1
    expected_output = ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    result = list(roman_range(start=7, stop=1, step=-1))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
    # Test generating Roman numerals from 1 to 8 with a step of 2
    expected_output = ['I', 'III', 'V', 'VII']
    result = list(roman_range(stop=8, step=2))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test generating Roman numerals from 1 to 7
        expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
        result = list(roman_range(7))
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
        # Test generating Roman numerals from 7 down to 1
        expected_output = ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
        result = list(roman_range(start=7, stop=1, step=-1))
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
        # Test generating Roman numerals from 1 to 8 with a step of 2
        expected_output = ['I', 'III', 'V', 'VII']
>       result = list(roman_range(stop=8, step=2))

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_edge_cases.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/generation.py:123: in generate
    yield roman_encode(current)
python-string-utils/string_utils/manipulation.py:634: in roman_encode
    return __RomanNumbers.encode(input_number)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__RomanNumbers'>, input_number = 4001

    @classmethod
    def encode(cls, input_number: Union[str, int]) -> str:
        # force input conversion to a string (we need it in order to iterate on each digit)
        input_string = str(input_number)
    
        if not is_integer(input_string):
            raise ValueError('Invalid input, only strings or integers are allowed')
    
        value = int(input_string)
    
        if value < 1 or value > 3999:
>           raise ValueError('Input must be >= 1 and <= 3999')
E           ValueError: Input must be >= 1 and <= 3999

python-string-utils/string_utils/manipulation.py:89: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""