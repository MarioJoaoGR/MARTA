
import pytest
from flutes.iterator import chunk

def test_valid_input():
    # Test with a valid range and n=3
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    # Test with a string and n=2
    result = list(chunk(2, "hello"))
    assert result == ["he", "ll", "o"]

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

flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with a valid range and n=3
        result = list(chunk(3, range(10)))
        assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
        # Test with a string and n=2
        result = list(chunk(2, "hello"))
>       assert result == ["he", "ll", "o"]
E       AssertionError: assert [['h', 'e'], ..., 'l'], ['o']] == ['he', 'll', 'o']
E         
E         At index 0 diff: ['h', 'e'] != 'he'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""