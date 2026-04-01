
import pytest
from flutes.iterator import Range

def test_valid_case_two_arguments():
    r = Range(1, 10)
    assert isinstance(r, Range)
    iterator = iter(r)
    values = []
    for _ in range(10):
        values.append(next(iterator))
    expected_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert values == expected_values

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___iter___1_test_valid_case_two_arguments.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_two_arguments _________________________

    def test_valid_case_two_arguments():
        r = Range(1, 10)
        assert isinstance(r, Range)
        iterator = iter(r)
        values = []
        for _ in range(10):
>           values.append(next(iterator))

flutes/Test4DT_tests/test_flutes_iterator_Range___iter___1_test_valid_case_two_arguments.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.Range object at 0x7fc32cfa2e90>

    def __next__(self) -> int:
        if self.val >= self.r:
>           raise StopIteration
E           StopIteration

flutes/flutes/iterator.py:335: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___iter___1_test_valid_case_two_arguments.py::test_valid_case_two_arguments
============================== 1 failed in 0.10s ===============================
"""