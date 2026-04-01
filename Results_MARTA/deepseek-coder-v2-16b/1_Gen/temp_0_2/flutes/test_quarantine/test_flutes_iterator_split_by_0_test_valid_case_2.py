
import pytest
from flutes.iterator import split_by

def test_valid_case_2():
    iterable = 'hello world'
    criterion = str.isspace
    expected_output = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    
    result = list(split_by(iterable, criterion=criterion))
    assert result == expected_output

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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        iterable = 'hello world'
        criterion = str.isspace
        expected_output = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    
        result = list(split_by(iterable, criterion=criterion))
>       assert result == expected_output
E       AssertionError: assert [['h', 'e', '...r', 'l', 'd']] == ['h', 'e', 'l...'o', ' ', ...]
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o'] != 'h'
E         Right contains 9 more items, first extra item: 'l'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_2.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_2.py::test_valid_case_2
============================== 1 failed in 0.09s ===============================
"""