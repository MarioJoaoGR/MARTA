
import pytest
from flutes.iterator import Range  # Assuming the module path is correct and 'Range' is defined there

def test_get_idx_valid():
    r = Range(0, 10)
    assert r._get_idx(0) == 0
    assert r._get_idx(2) == 4
    assert r._get_idx(4) == 8

def test_get_idx_invalid():
    r = Range(0, 10)
    with pytest.raises(IndexError):
        r._get_idx(-1)  # Negative index should raise an IndexError
    with pytest.raises(IndexError):
        r._get_idx(5)   # Index out of range should raise an IndexError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_get_idx_valid ______________________________

    def test_get_idx_valid():
        r = Range(0, 10)
        assert r._get_idx(0) == 0
>       assert r._get_idx(2) == 4
E       assert 2 == 4
E        +  where 2 = _get_idx(2)
E        +    where _get_idx = <flutes.iterator.Range object at 0x7fccba786250>._get_idx

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py:8: AssertionError
_____________________________ test_get_idx_invalid _____________________________

    def test_get_idx_invalid():
        r = Range(0, 10)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py::test_get_idx_valid
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py::test_get_idx_invalid
============================== 2 failed in 0.08s ===============================

"""