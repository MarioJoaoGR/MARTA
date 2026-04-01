
import pytest
from io import StringIO
from isort.core import process

def test_error_handling():
    input_stream = StringIO("# This is a skip comment\n# isort: off\nimport os\n")
    output_stream = StringIO()
    
    with pytest.raises(ValueError):
        process(input_stream, output_stream)

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

isort/Test4DT_tests/test_isort_core_process_1_test_error_handling.py F   [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        input_stream = StringIO("# This is a skip comment\n# isort: off\nimport os\n")
        output_stream = StringIO()
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_core_process_1_test_error_handling.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_core_process_1_test_error_handling.py::test_error_handling
============================== 1 failed in 0.13s ===============================
"""