
import pytest
import logging
from pytutils.log import logger_level

def test_logger_level_edge_cases():
    log = logging.getLogger(__name__)
    
    # Test with None level
    with pytest.raises(TypeError):
        with logger_level(log, None):
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________ test_logger_level_edge_cases _________________________

    def test_logger_level_edge_cases():
        log = logging.getLogger(__name__)
    
        # Test with None level
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py::test_logger_level_edge_cases
============================== 1 failed in 0.05s ===============================
"""