
import os
from pathlib import Path
import pytest
from unittest.mock import patch
from httpie.config import get_default_config_dir, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_HTTPIE_CONFIG_DIR, is_windows, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

@pytest.mark.skipif(os.name == 'nt', reason="This test is for non-Windows systems")
def test_invalid_input():
    with patch('os.environ', {}):
        config_dir = get_default_config_dir()
        assert isinstance(config_dir, Path), "Expected a Path object"
        expected_path = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        assert config_dir == expected_path, f"Expected {expected_path}, but got {config_dir}"

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

httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    @pytest.mark.skipif(os.name == 'nt', reason="This test is for non-Windows systems")
    def test_invalid_input():
        with patch('os.environ', {}):
            config_dir = get_default_config_dir()
            assert isinstance(config_dir, Path), "Expected a Path object"
            expected_path = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
>           assert config_dir == expected_path, f"Expected {expected_path}, but got {config_dir}"
E           AssertionError: Expected /home/joaovitorino/.httpie, but got /home/joaovitorino/.config/httpie
E           assert PosixPath('/home/joaovitorino/.config/httpie') == PosixPath('/home/joaovitorino/.httpie')

httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_invalid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""