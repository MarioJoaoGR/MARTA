
import pytest
from flutes.iterator import Range

# Test case to cover line 334-338 (if self.val >= self.r)
def test_range_next_raises_stopiteration():
    r = Range(10)
    with pytest.raises(StopIteration):
        next(r)
        next(r)
        next(r)  # Should raise StopIteration after reaching the end of the range

# Test case to cover line 334-338 (if self.val >= self.r) with a different start and step
def test_range_next_raises_stopiteration_with_different_params():
    r = Range(5, 10, 2)  # Start at 5, end at 10, step by 2
    with pytest.raises(StopIteration):
        next(r)
        next(r)  # Should raise StopIteration after reaching the end of the range

# Test case to cover line 336 (self.val += self.step)
def test_range_next_increments_correctly():
    r = Range(0, 5)  # Start at 0, end at 5, step by default 1
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_Range___next___1.py FF.        [100%]

=================================== FAILURES ===================================
_____________________ test_range_next_raises_stopiteration _____________________

    def test_range_next_raises_stopiteration():
        r = Range(10)
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_iterator_Range___next___1.py:8: Failed
__________ test_range_next_raises_stopiteration_with_different_params __________

    def test_range_next_raises_stopiteration_with_different_params():
        r = Range(5, 10, 2)  # Start at 5, end at 10, step by 2
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_iterator_Range___next___1.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___next___1.py::test_range_next_raises_stopiteration
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___next___1.py::test_range_next_raises_stopiteration_with_different_params
========================= 2 failed, 1 passed in 0.09s ==========================
"""