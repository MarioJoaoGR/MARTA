
from string_utils.generation import roman_range
import pytest

def test_invalid_inputs():
    with pytest.raises(ValueError):
        list(roman_range(-1))  # Invalid stop value

    with pytest.raises(ValueError):
        list(roman_range(stop=5, start=-1))  # Invalid start value

    with pytest.raises(ValueError):
        list(roman_range(stop=5, start=1, step="invalid"))  # Invalid step value

    with pytest.raises(OverflowError):
        list(roman_range(start=3, stop=2))  # Step leads to no iteration

    with pytest.raises(OverflowError):
        list(roman_range(stop=8, start=10, step=-1))  # Step leads to no iteration in reverse

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            list(roman_range(-1))  # Invalid stop value
    
        with pytest.raises(ValueError):
            list(roman_range(stop=5, start=-1))  # Invalid start value
    
        with pytest.raises(ValueError):
            list(roman_range(stop=5, start=1, step="invalid"))  # Invalid step value
    
        with pytest.raises(OverflowError):
            list(roman_range(start=3, stop=2))  # Step leads to no iteration
    
>       with pytest.raises(OverflowError):
E       Failed: DID NOT RAISE <class 'OverflowError'>

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""