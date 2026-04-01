
import pytest
from flutes.iterator import split_by

def test_edge_case_empty_segments():
    iterable = [1, 3, 5, 6, 7]
    criterion = lambda x: x > 4
    empty_segments = True
    
    result = list(split_by(iterable, criterion=criterion, empty_segments=empty_segments))
    expected = [[6], [], [7]]
    
    assert result == expected

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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py F [100%]

=================================== FAILURES ===================================
________________________ test_edge_case_empty_segments _________________________

    def test_edge_case_empty_segments():
        iterable = [1, 3, 5, 6, 7]
        criterion = lambda x: x > 4
        empty_segments = True
    
        result = list(split_by(iterable, criterion=criterion, empty_segments=empty_segments))
        expected = [[6], [], [7]]
    
>       assert result == expected
E       assert [[1, 3], [], [], []] == [[6], [], [7]]
E         
E         At index 0 diff: [1, 3] != [6]
E         Left contains one more item: []
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py::test_edge_case_empty_segments
============================== 1 failed in 0.09s ===============================
"""