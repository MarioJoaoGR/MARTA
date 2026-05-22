
import pytest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR

def test_valid_case():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', 'custom_dir'):
        config = Config()
        assert config.version_info_file() == Path('custom_dir/version_info.json')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_config_Config_version_info_file_0_test_valid_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config_version_info_file_0_test_valid_case.py:9:15: E1102: config.version_info_file is not callable (not-callable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config_version_info_file_0_test_valid_case.py:9:45: E0602: Undefined variable 'Path' (undefined-variable)


"""