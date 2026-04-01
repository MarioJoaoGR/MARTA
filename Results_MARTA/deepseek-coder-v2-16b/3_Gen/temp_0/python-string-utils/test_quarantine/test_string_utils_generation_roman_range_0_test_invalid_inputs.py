
from string_utils.generation import roman_range
import pytest

def test_invalid_inputs():
    # Test when stop is not an integer
    with pytest.raises(ValueError):
        list(roman_range("stop"))
    
    # Test when start is not an integer
    with pytest.raises(ValueError):
        list(roman_range(stop=10, start="start"))
    
    # Test when step is not an integer
    with pytest.raises(ValueError):
        list(roman_range(stop=10, start=1, step="step"))
    
    # Test when stop is less than or equal to 0
    with pytest.raises(ValueError):
        list(roman_range(stop=0))
    
    # Test when start is less than or equal to 0
    with pytest.raises(ValueError):
        list(roman_range(stop=10, start=0))
    
    # Test when step is zero (invalid configuration)
    with pytest.raises(OverflowError):
        list(roman_range(stop=10, start=1, step=0))
    
    # Test when stop is less than start and step is positive (invalid configuration)
    with pytest.raises(OverflowError):
        list(roman_range(stop=5, start=10, step=1))
    
    # Test when start is greater than stop and step is negative (invalid configuration)
    with pytest.raises(OverflowError):
        list(roman_range(stop=5, start=10, step=-1))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test when stop is not an integer
        with pytest.raises(ValueError):
            list(roman_range("stop"))
    
        # Test when start is not an integer
        with pytest.raises(ValueError):
            list(roman_range(stop=10, start="start"))
    
        # Test when step is not an integer
        with pytest.raises(ValueError):
            list(roman_range(stop=10, start=1, step="step"))
    
        # Test when stop is less than or equal to 0
        with pytest.raises(ValueError):
            list(roman_range(stop=0))
    
        # Test when start is less than or equal to 0
        with pytest.raises(ValueError):
            list(roman_range(stop=10, start=0))
    
        # Test when step is zero (invalid configuration)
        with pytest.raises(OverflowError):
>           list(roman_range(stop=10, start=1, step=0))

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_invalid_inputs.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/generation.py:132: in roman_range
    validate(step, 'step', allow_negative=True)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

arg_value = 0, arg_name = 'step', allow_negative = True

    def validate(arg_value, arg_name, allow_negative=False):
        msg = '"{}" must be an integer in the range 1-3999'.format(arg_name)
    
        if not isinstance(arg_value, int):
            raise ValueError(msg)
    
        if allow_negative:
            arg_value = abs(arg_value)
    
        if arg_value < 1 or arg_value > 3999:
>           raise ValueError(msg)
E           ValueError: "step" must be an integer in the range 1-3999

python-string-utils/string_utils/generation.py:116: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""