
import os
from pathlib import Path
from unittest.mock import patch
from httpie.config import get_default_config_dir, ENV_HTTPIE_CONFIG_DIR, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

def test_invalid_input():
    with patch('os.environ', {}):  # Unset all environment variables
        config_dir = get_default_config_dir()
        assert str(config_dir) == str(Path.home() / '.httpie')

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('os.environ', {}):  # Unset all environment variables
            config_dir = get_default_config_dir()
>           assert str(config_dir) == str(Path.home() / '.httpie')
E           AssertionError: assert '/home/joaovi...config/httpie' == '/home/joaovitorino/.httpie'
E             
E             - /home/joaovitorino/.httpie
E             + /home/joaovitorino/.config/httpie
E             ?                     +++++++

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_2_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.14s ===============================
"""