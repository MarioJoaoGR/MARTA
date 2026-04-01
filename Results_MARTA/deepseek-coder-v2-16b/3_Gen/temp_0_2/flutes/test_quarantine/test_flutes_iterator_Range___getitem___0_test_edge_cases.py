
import pytest
from flutes.iterator import Range

def test_slice_with_step():
    r = Range(1, 11, 2)
    assert r[0:5:2] == [1, 3, 5, 7, 9]

def test_invalid_index():
    r = Range(10)
    with pytest.raises(IndexError):
        r[-1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_slice_with_step _____________________________

    def test_slice_with_step():
        r = Range(1, 11, 2)
>       assert r[0:5:2] == [1, 3, 5, 7, 9]
E       assert [1, 5, 9] == [1, 3, 5, 7, 9]
E         
E         At index 1 diff: 5 != 3
E         Right contains 2 more items, first extra item: 7
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_edge_cases.py:7: AssertionError
______________________________ test_invalid_index ______________________________

    def test_invalid_index():
        r = Range(10)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_edge_cases.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_edge_cases.py::test_slice_with_step
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_edge_cases.py::test_invalid_index
============================== 2 failed in 0.11s ===============================
"""