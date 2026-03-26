
import logging
from pytutils.log import configure, DEFAULT_CONFIG, get_config

def test_valid_inputs():
    log = logging.getLogger(__name__)
    configure()
    assert len(log.handlers) == 1, "Expected one handler to be configured"

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

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        log = logging.getLogger(__name__)
        configure()
>       assert len(log.handlers) == 1, "Expected one handler to be configured"
E       AssertionError: Expected one handler to be configured
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = <Logger Test4DT_tests.test_pytutils_log_configure_0_test_valid_inputs (DEBUG)>.handlers

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.06s ===============================
"""