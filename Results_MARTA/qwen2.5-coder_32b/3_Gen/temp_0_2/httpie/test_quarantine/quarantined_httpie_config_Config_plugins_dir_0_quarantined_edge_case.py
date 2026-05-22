
import pytest
from unittest.mock import patch
from httpie.config import DEFAULT_CONFIG_DIR, Config
from pathlib import Path

def test_plugins_dir():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', new=Path('/custom/directory')):
        config = Config()
        assert config.plugins_dir() == Path('/custom/directory') / 'plugins'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_Config_plugins_dir_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_Config_plugins_dir_0_test_edge_case.py:10:15: E1102: config.plugins_dir is not callable (not-callable)


"""