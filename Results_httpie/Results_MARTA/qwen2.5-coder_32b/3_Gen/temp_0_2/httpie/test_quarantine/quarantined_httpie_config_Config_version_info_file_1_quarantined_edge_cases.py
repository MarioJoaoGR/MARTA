
import pytest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR

def test_version_info_file():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', 'custom_dir'):
        config = Config()
        assert config.version_info_file() == Path('custom_dir/version_info.json')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_Config_version_info_file_1_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_Config_version_info_file_1_test_edge_cases.py:9:15: E1102: config.version_info_file is not callable (not-callable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_Config_version_info_file_1_test_edge_cases.py:9:45: E0602: Undefined variable 'Path' (undefined-variable)


"""