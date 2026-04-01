
from io import StringIO
import pytest
from isort.core import process
from isort.exceptions import FileSkipComment
from isort.settings import Config, DEFAULT_CONFIG

def test_error_case():
    input_stream = StringIO("# isort: off\nprint('Hello, World!')")
    output_stream = StringIO()
    
    with pytest.raises(FileSkipComment):
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

isort/Test4DT_tests/test_isort_core_process_1_test_error_case.py F       [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        input_stream = StringIO("# isort: off\nprint('Hello, World!')")
        output_stream = StringIO()
    
>       with pytest.raises(FileSkipComment):
E       Failed: DID NOT RAISE <class 'isort.exceptions.FileSkipComment'>

isort/Test4DT_tests/test_isort_core_process_1_test_error_case.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_core_process_1_test_error_case.py::test_error_case
============================== 1 failed in 0.10s ===============================
"""