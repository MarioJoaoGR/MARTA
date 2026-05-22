
import unittest
from unittest.mock import patch, MagicMock
from httpie.config import Config

class TestConfig(unittest.TestCase):
    @patch('httpie.config.DEFAULT_CONFIG_DIR', '/default/config/dir')
    def test_invalid_input(self):
        config = Config()
        with self.assertRaises(TypeError):
            config.plugins_dir()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_config_Config_plugins_dir_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_config_Config_plugins_dir_0_test_invalid_input.py:11:12: E1102: config.plugins_dir is not callable (not-callable)


"""