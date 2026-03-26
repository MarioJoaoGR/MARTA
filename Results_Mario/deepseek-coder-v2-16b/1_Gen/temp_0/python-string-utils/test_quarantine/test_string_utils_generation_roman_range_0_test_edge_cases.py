
import pytest
from string_utils.generation import roman_range, roman_encode

def test_edge_cases():
    # Test start equals stop
    with pytest.raises(StopIteration):
        gen = roman_range(start=1, stop=1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test start equals stop
        with pytest.raises(StopIteration):
>           gen = roman_range(start=1, stop=1)

python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

stop = 1, start = 1, step = 1

    def roman_range(stop: int, start: int = 1, step: int = 1) -> Generator:
        """
        Similarly to native Python's `range()`, returns a Generator object which generates a new roman number
        on each iteration instead of an integer.
    
        *Example:*
    
        >>> for n in roman_range(7): print(n)
        >>> # prints: I, II, III, IV, V, VI, VII
        >>> for n in roman_range(start=7, stop=1, step=-1): print(n)
        >>> # prints: VII, VI, V, IV, III, II, I
    
        :param stop: Number at which the generation must stop (must be <= 3999).
        :param start: Number at which the generation must start (must be >= 1).
        :param step: Increment of each generation step (default to 1).
        :return: Generator of roman numbers.
        """
    
        def validate(arg_value, arg_name, allow_negative=False):
            msg = '"{}" must be an integer in the range 1-3999'.format(arg_name)
    
            if not isinstance(arg_value, int):
                raise ValueError(msg)
    
            if allow_negative:
                arg_value = abs(arg_value)
    
            if arg_value < 1 or arg_value > 3999:
                raise ValueError(msg)
    
        def generate():
            current = start
    
            # generate values for each step
            while current != stop:
                yield roman_encode(current)
                current += step
    
            # last value to return
            yield roman_encode(current)
    
        # checks each single argument value
        validate(stop, 'stop')
        validate(start, 'start')
        validate(step, 'step', allow_negative=True)
    
        # checks if the provided configuration leads to a feasible iteration with respect to boundaries or not
        forward_exceed = step > 0 and (start > stop or start + step > stop)
        backward_exceed = step < 0 and (start < stop or start + step < stop)
        if forward_exceed or backward_exceed:
>           raise OverflowError('Invalid start/stop/step configuration')
E           OverflowError: Invalid start/stop/step configuration

python-string-utils/string_utils/generation.py:138: OverflowError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================

"""