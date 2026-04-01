
import pytest
import os
from pytutils.log import get_config

def test_invalid_inputs():
    # Test when given is None, env_var is set, and default is None
    os.environ['CONFIG'] = '{"key": "value"}'
    with pytest.raises(ValueError):
        assert get_config() == {'key': 'value'}
    
    # Test when given is an empty dictionary, env_var is set, and default is None
    with pytest.raises(ValueError):
        assert get_config(given={}) == {}

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

pytutils/Test4DT_tests/test_pytutils_log_get_config_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test when given is None, env_var is set, and default is None
        os.environ['CONFIG'] = '{"key": "value"}'
        with pytest.raises(ValueError):
            assert get_config() == {'key': 'value'}
    
        # Test when given is an empty dictionary, env_var is set, and default is None
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_log_get_config_1_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""