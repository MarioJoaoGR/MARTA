
from io import StringIO
from pathlib import Path
import pytest
from isort.api import find_imports_in_stream, Config, ImportKey

def test_find_imports_in_stream_with_none():
    with pytest.raises(TypeError):
        find_imports_in_stream(None)

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

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
____________________ test_find_imports_in_stream_with_none _____________________

    def test_find_imports_in_stream_with_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_0_test_edge_case_none.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_0_test_edge_case_none.py::test_find_imports_in_stream_with_none
============================== 1 failed in 0.10s ===============================
"""