
import pytest
from flutes.iterator import split_by

def test_valid_case_criterion():
    # Test case where criterion is used to split the iterable
    result = list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5]]
    
    # Test case with empty segments allowed and criterion used
    result = list(split_by([1, 2, 3, 4, 5], empty_segments=True, criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5]]
    
    # Test case with separator used to split the iterable
    result = list(split_by("Split by:", separator=' '))
    assert result == ["Split", "by:"]

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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_criterion.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_criterion ___________________________

    def test_valid_case_criterion():
        # Test case where criterion is used to split the iterable
        result = list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 3 == 0))
        assert result == [[1, 2], [4, 5]]
    
        # Test case with empty segments allowed and criterion used
        result = list(split_by([1, 2, 3, 4, 5], empty_segments=True, criterion=lambda x: x % 3 == 0))
        assert result == [[1, 2], [4, 5]]
    
        # Test case with separator used to split the iterable
        result = list(split_by("Split by:", separator=' '))
>       assert result == ["Split", "by:"]
E       AssertionError: assert [['S', 'p', '...b', 'y', ':']] == ['Split', 'by:']
E         
E         At index 0 diff: ['S', 'p', 'l', 'i', 't'] != 'Split'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_criterion.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_criterion.py::test_valid_case_criterion
============================== 1 failed in 0.08s ===============================
"""