
import pytest
from flutes.iterator import split_by

def test_valid_input_happy_path():
    # Test splitting a list by a specific separator
    assert list(split_by([1, 2, 3, 4], separator=2)) == [[1], [3, 4]]
    
    # Test splitting a string by a space separator
    assert list(split_by("hello world", separator=" ")) == ['hello', 'world']
    
    # Additional test to ensure it handles strings correctly
    assert list(split_by("a b c d", separator=" ")) == ["a", "b", "c", "d"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test splitting a list by a specific separator
        assert list(split_by([1, 2, 3, 4], separator=2)) == [[1], [3, 4]]
    
        # Test splitting a string by a space separator
>       assert list(split_by("hello world", separator=" ")) == ['hello', 'world']
E       AssertionError: assert [['h', 'e', '...r', 'l', 'd']] == ['hello', 'world']
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o'] != 'hello'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.08s ===============================
"""