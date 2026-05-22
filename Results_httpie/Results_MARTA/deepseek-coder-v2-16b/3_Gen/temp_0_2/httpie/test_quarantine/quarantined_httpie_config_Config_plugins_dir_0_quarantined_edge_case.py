
import unittest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR
from pathlib import Path

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    @patch('httpie.config.DEFAULT_CONFIG_DIR', 'custom_dir')
    def test_plugins_dir_default_directory(self):
        with patch.object(Config, '_configured_path', return_value=Path('custom_dir/plugins')):
            self.assertEqual(self.config.plugins_dir(), Path('custom_dir/plugins'))

    @patch('httpie.config.DEFAULT_CONFIG_DIR', 'default_dir')
    def test_plugins_dir_with_directory(self):
        config = Config('custom_dir')
        with patch.object(Config, '_configured_path', return_value=Path('custom_dir/plugins')):
            self.assertEqual(config.plugins_dir(), Path('custom_dir/plugins'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_config_Config_plugins_dir_0_test_edge_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config_plugins_dir_0_test_edge_case.py:14:29: E1102: self.config.plugins_dir is not callable (not-callable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_Config_plugins_dir_0_test_edge_case.py:20:29: E1102: config.plugins_dir is not callable (not-callable)


"""