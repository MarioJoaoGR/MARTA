
import pytest
from flutes.iterator import Range

def test_invalid_index():
    r = Range(10)
    with pytest.raises(IndexError):
        r[10]  # This should raise an IndexError because the index is out of range

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_index ______________________________

    def test_invalid_index():
        r = Range(10)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py::test_invalid_index
============================== 1 failed in 0.10s ===============================
"""