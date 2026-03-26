
import pytest
from isort.sorting import naturally, _natural_keys

def test_valid_input():
    # Test case with default settings
    assert naturally(['item12', 'item2', 'item1']) == ['item1', 'item2', 'item12']
    
    # Test case with key function provided
    assert naturally(['file10.txt', 'file2.txt', 'file1.txt'], key=lambda x: x.split('.')[-1]) == ['file1.txt', 'file2.txt', 'file10.txt']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case with default settings
        assert naturally(['item12', 'item2', 'item1']) == ['item1', 'item2', 'item12']
    
        # Test case with key function provided
>       assert naturally(['file10.txt', 'file2.txt', 'file1.txt'], key=lambda x: x.split('.')[-1]) == ['file1.txt', 'file2.txt', 'file10.txt']
E       AssertionError: assert ['file10.txt'..., 'file1.txt'] == ['file1.txt',... 'file10.txt']
E         
E         At index 0 diff: 'file10.txt' != 'file1.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting_naturally_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""