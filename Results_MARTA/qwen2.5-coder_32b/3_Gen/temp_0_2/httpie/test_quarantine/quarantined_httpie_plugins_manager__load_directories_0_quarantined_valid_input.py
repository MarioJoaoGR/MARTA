
import unittest
from pathlib import Path
from httpie.plugins.manager import _load_directories
from unittest.mock import patch, MagicMock

class TestHttpiePluginsManagerLoadDirectories(unittest.TestCase):
    @patch('sys.path', [])
    def test_valid_input(self, mock_sys_path):
        site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
        with patch('os.fspath', side_effect=lambda p: str(p)) as mock_fspath:
            gen = _load_directories(site_dirs)
            next(gen)  # Start the generator
            
            self.assertIn('/path/to/site1', sys.path)
            self.assertIn('/path/to/site2', sys.path)
            
            mock_fspath.assert_any_call(Path('/path/to/site1'))
            mock_fspath.assert_any_call(Path('/path/to/site2'))
            
            next(gen)  # Trigger the finally block to remove paths from sys.path
            
            self.assertNotIn('/path/to/site1', sys.path)
            self.assertNotIn('/path/to/site2', sys.path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager__load_directories_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_valid_input.py:15:44: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_valid_input.py:16:44: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_valid_input.py:23:47: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_valid_input.py:24:47: E0602: Undefined variable 'sys' (undefined-variable)


"""