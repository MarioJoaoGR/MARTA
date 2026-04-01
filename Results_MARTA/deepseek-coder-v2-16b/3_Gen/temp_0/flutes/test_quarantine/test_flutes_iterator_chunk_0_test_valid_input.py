
import pytest
from flutes.iterator import chunk

def test_valid_input():
    # Test with a list of numbers
    iterable = range(10)
    n = 3
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output
    
    # Test with a string
    iterable = "abcdefghij"
    n = 4
    expected_output = ["abcd", "efgh", "ij"]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_chunk_0_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with a list of numbers
        iterable = range(10)
        n = 3
        expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
        result = list(chunk(n, iterable))
        assert result == expected_output
    
        # Test with a string
        iterable = "abcdefghij"
        n = 4
        expected_output = ["abcd", "efgh", "ij"]
    
        result = list(chunk(n, iterable))
>       assert result == expected_output
E       AssertionError: assert [['a', 'b', '...], ['i', 'j']] == ['abcd', 'efgh', 'ij']
E         
E         At index 0 diff: ['a', 'b', 'c', 'd'] != 'abcd'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_chunk_0_test_valid_input.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_chunk_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""