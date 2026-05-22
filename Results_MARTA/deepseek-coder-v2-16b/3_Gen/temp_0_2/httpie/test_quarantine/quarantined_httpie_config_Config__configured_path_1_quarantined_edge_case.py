
import pytest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR
from pathlib import Path

class TestConfig:
    @patch('httpie.config.DEFAULT_CONFIG_DIR', 'default_dir')
    def test_edge_case(self):
        config = Config()
        assert config.directory == Path('default_dir'), f"Expected directory to be 'default_dir' but got {config.directory}"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config__configured_path_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________ TestConfig.test_edge_case ___________________________

self = <test_httpie_config_Config__configured_path_1_test_edge_case.TestConfig object at 0x7f4e65377e90>

    @patch('httpie.config.DEFAULT_CONFIG_DIR', 'default_dir')
    def test_edge_case(self):
        config = Config()
>       assert config.directory == Path('default_dir'), f"Expected directory to be 'default_dir' but got {config.directory}"
E       AssertionError: Expected directory to be 'default_dir' but got /home/joaovitorino/.config/httpie
E       assert PosixPath('/home/joaovitorino/.config/httpie') == PosixPath('default_dir')
E        +  where PosixPath('/home/joaovitorino/.config/httpie') = {'default_options': []}.directory
E        +  and   PosixPath('default_dir') = Path('default_dir')

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config__configured_path_1_test_edge_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config__configured_path_1_test_edge_case.py::TestConfig::test_edge_case
============================== 1 failed in 0.08s ===============================
"""