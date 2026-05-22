
import unittest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

class TestEnvironmentConfig(unittest.TestCase):
    @patch('httpie.context.sys')
    def test_config_dir_default(self, mock_sys):
        env = Environment()
        self.assertEqual(env.config_dir, Environment.DEFAULT_CONFIG_DIR)

    @patch('httpie.context.ConfigFileError', MagicMock())
    @patch('httpie.context.Config')
    def test_load_config_file_error(self, mock_Config):
        env = Environment()
        mock_Config.return_value.is_new.return_value = False
        mock_Config.return_value.load.side_effect = ConfigFileError("Test error")
        
        with patch('httpie.context.LogLevel', MagicMock()) as mock_log:
            env.config()
            mock_Config.return_value.load.assert_called_once()
            mock_log.log_error.assert_called_with("Test error", level=mock_log.LogLevel.WARNING)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_context_Environment_config_2_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_config_2_test_edge_cases.py:10:41: E1101: Class 'Environment' has no 'DEFAULT_CONFIG_DIR' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_config_2_test_edge_cases.py:17:52: E0602: Undefined variable 'ConfigFileError' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_config_2_test_edge_cases.py:20:12: E1102: env.config is not callable (not-callable)


"""