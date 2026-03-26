
import pytest
from unittest.mock import patch
import logging
from pytutils.log import configure, DEFAULT_CONFIG

def get_config(config=None, env_var='LOGGING', default=DEFAULT_CONFIG):
    # Mock implementation for the purpose of this test
    return config if config is not None else DEFAULT_CONFIG

@pytest.fixture(autouse=True)
def setup_logging():
    logging.getLogger().handlers = []  # Clear any existing handlers to avoid interference

@patch('pytutils.log.get_config', side_effect=get_config)
def test_invalid_inputs(*mocks):
    with pytest.raises(Exception):
        configure()

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

pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

mocks = (<MagicMock name='get_config' id='140521595234704'>,)

    @patch('pytutils.log.get_config', side_effect=get_config)
    def test_invalid_inputs(*mocks):
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_invalid_inputs.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""