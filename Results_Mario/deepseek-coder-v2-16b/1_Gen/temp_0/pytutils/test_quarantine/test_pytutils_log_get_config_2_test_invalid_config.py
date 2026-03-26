
import pytest
from pytutils.log import get_config
import os

def test_invalid_config():
    with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
        get_config()

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

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_config ______________________________

    def test_invalid_config():
        with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
>           get_config()

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = None, default = None

    def get_config(given=None, env_var=None, default=None):
        config = given
    
        if not config and env_var:
            config = os.environ.get(env_var)
    
        if not config and default:
            config = default
    
        if config is None:
>           raise ValueError('Invalid logging config: %s' % config)
E           ValueError: Invalid logging config: None

pytutils/pytutils/log.py:114: ValueError

During handling of the above exception, another exception occurred:

    def test_invalid_config():
>       with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
E       AssertionError: Regex pattern did not match.
E        Regex: 'Could not parse logging config as bare, json, or yaml: invalid'
E        Input: 'Invalid logging config: None'

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py::test_invalid_config
============================== 1 failed in 0.06s ===============================
"""