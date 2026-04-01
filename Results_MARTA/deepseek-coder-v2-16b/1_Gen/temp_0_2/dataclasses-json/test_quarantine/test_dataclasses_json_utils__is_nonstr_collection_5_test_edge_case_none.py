
import pytest
from dataclasses_json.utils import _is_nonstr_collection

def test_edge_case_none():
    with pytest.raises(TypeError):
        assert _is_nonstr_collection(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(TypeError):
>           assert _is_nonstr_collection(None)
E           assert False
E            +  where False = _is_nonstr_collection(None)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================
"""