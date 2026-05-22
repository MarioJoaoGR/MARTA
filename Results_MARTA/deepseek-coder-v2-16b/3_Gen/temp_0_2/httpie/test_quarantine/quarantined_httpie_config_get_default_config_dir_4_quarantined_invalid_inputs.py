
import os
from pathlib import Path
import pytest
from unittest.mock import patch
from httpie.config import get_default_config_dir, DEFAULT_WINDOWS_CONFIG_DIR, ENV_HTTPIE_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

def test_invalid_inputs():
    with patch.dict(os.environ, {}):  # Clear environment variables
        with pytest.raises(FileNotFoundError):  # Expect an error due to missing config directory
            get_default_config_dir()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_4_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch.dict(os.environ, {}):  # Clear environment variables
>           with pytest.raises(FileNotFoundError):  # Expect an error due to missing config directory
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_4_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_4_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.17s ===============================
"""