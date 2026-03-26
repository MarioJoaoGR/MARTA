
import pytest
from flutes.iterator import Range

def test_range_negative_indexing():
    r = Range(10)
    with pytest.raises(IndexError):
        r[-1]  # This should raise an IndexError because negative indexing is not supported by the current implementation

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___3_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________ test_range_negative_indexing _________________________

    def test_range_negative_indexing():
        r = Range(10)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___3_test_edge_cases.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___3_test_edge_cases.py::test_range_negative_indexing
============================== 1 failed in 0.11s ===============================
"""