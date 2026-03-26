
import pytest
from flutes.iterator import split_by

def test_valid_input_list():
    iterable = [1, 2, 3, 4, 5]
    separator = 3
    
    result = list(split_by(iterable, empty_segments=False, separator=separator))
    assert result == [[1, 2], [4, 5]]
    
    result_with_empty = list(split_by(iterable, empty_segments=True, separator=separator))
    assert result_with_empty == [[1, 2], [], [4, 5]]

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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_list.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_list _____________________________

    def test_valid_input_list():
        iterable = [1, 2, 3, 4, 5]
        separator = 3
    
        result = list(split_by(iterable, empty_segments=False, separator=separator))
        assert result == [[1, 2], [4, 5]]
    
        result_with_empty = list(split_by(iterable, empty_segments=True, separator=separator))
>       assert result_with_empty == [[1, 2], [], [4, 5]]
E       assert [[1, 2], [4, 5]] == [[1, 2], [], [4, 5]]
E         
E         At index 1 diff: [4, 5] != []
E         Right contains one more item: [4, 5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_list.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_list.py::test_valid_input_list
============================== 1 failed in 0.09s ===============================
"""