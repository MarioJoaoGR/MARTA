
import pytest
from flutes.iterator import split_by

def test_valid_case_separator():
    iterable = " Split by: "
    empty_segments = True
    separator = '.'
    
    result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
    expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_valid_case_separator.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_separator ___________________________

    def test_valid_case_separator():
        iterable = " Split by: "
        empty_segments = True
        separator = '.'
    
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
        expected = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    
>       assert result == expected
E       AssertionError: assert [[' ', 'S', '...i', 't', ...]] == [[], ['S', 'p...'y', ':'], []]
E         
E         At index 0 diff: [' ', 'S', 'p', 'l', 'i', 't', ' ', 'b', 'y', ':', ' '] != []
E         Right contains 3 more items, first extra item: ['S', 'p', 'l', 'i', 't']
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_valid_case_separator.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_valid_case_separator.py::test_valid_case_separator
============================== 1 failed in 0.10s ===============================

"""