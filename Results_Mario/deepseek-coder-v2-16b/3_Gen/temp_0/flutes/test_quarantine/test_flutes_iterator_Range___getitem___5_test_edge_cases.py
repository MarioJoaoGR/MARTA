
import pytest
from flutes.iterator import Range

def test_range_with_start_end_negative_index():
    r = Range(1, 10 + 1)
    assert r[-1] == 10, "Negative indexing should work correctly for a range with start and end"
    assert r[-3] == 9, "Negative indexing with step size of 1 and second argument as end"

def test_range_with_start_end_step_negative_index():
    r = Range(1, 11, 2)
    assert r[-1] == 10, "Negative indexing should work correctly for a range with start, end, and step"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_range_with_start_end_negative_index ___________________

    def test_range_with_start_end_negative_index():
        r = Range(1, 10 + 1)
        assert r[-1] == 10, "Negative indexing should work correctly for a range with start and end"
>       assert r[-3] == 9, "Negative indexing with step size of 1 and second argument as end"
E       AssertionError: Negative indexing with step size of 1 and second argument as end
E       assert 8 == 9

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_edge_cases.py:8: AssertionError
________________ test_range_with_start_end_step_negative_index _________________

    def test_range_with_start_end_step_negative_index():
        r = Range(1, 11, 2)
>       assert r[-1] == 10, "Negative indexing should work correctly for a range with start, end, and step"
E       AssertionError: Negative indexing should work correctly for a range with start, end, and step
E       assert 9 == 10

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_edge_cases.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_edge_cases.py::test_range_with_start_end_negative_index
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_edge_cases.py::test_range_with_start_end_step_negative_index
============================== 2 failed in 0.12s ===============================
"""