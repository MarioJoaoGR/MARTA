
import pytest
from isort.literal import register_type, type_mapping

def test_edge_case_none():
    with pytest.raises(KeyError):
        @register_type("test_none", type(None))
        def sort_function(value, printer):
            return "sorted_none"

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

isort/Test4DT_tests/test_isort_literal_register_type_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort_literal_register_type_0_test_edge_case_none.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal_register_type_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.14s ===============================
"""