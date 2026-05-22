
import unittest
from unittest.mock import patch, MagicMock
from httpie.config import Config

class TestConfig(unittest.TestCase):
    @patch('httpie.config.DEFAULT_CONFIG_DIR', '/default/config/dir')
    def test_plugins_dir(self):
        config = Config()
        with patch.object(config, '_configured_path', return_value='/custom/plugins/dir'):
            self.assertEqual(config.plugins_dir(), Path('/custom/plugins/dir'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_Config_plugins_dir_0_test_valid_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_Config_plugins_dir_0_test_valid_case.py:11:29: E1102: config.plugins_dir is not callable (not-callable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_Config_plugins_dir_0_test_valid_case.py:11:51: E0602: Undefined variable 'Path' (undefined-variable)


"""