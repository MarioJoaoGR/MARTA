
import os
from pathlib import Path
from unittest.mock import patch
from httpie.config import get_default_config_dir, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_HTTPIE_CONFIG_DIR

def test_edge_case_none():
    with patch('os.environ', {}):
        config_dir = get_default_config_dir()
        assert isinstance(config_dir, Path)
        home_dir = Path.home()
        expected_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        assert config_dir == expected_dir

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

httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with patch('os.environ', {}):
            config_dir = get_default_config_dir()
            assert isinstance(config_dir, Path)
            home_dir = Path.home()
            expected_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
>           assert config_dir == expected_dir
E           AssertionError: assert PosixPath('/home/joaovitorino/.config/httpie') == PosixPath('/home/joaovitorino/.httpie')

httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_edge_case_none.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_2_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.11s ===============================
"""