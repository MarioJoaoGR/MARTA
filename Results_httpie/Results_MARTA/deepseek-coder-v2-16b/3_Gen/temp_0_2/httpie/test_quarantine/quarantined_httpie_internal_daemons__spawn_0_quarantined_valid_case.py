
import unittest
from unittest.mock import patch, MagicMock
from httpie.internal.daemons import _spawn_windows, _spawn_posix
from httpie.contexts import ProcessContext

class TestHttpieInternalDaemonsSpawn0TestCase(unittest.TestCase):
    @patch('httpie.internal.daemons._spawn_windows')
    @patch('httpie.internal.daemons._spawn_posix')
    def test_valid_case(self, mock_spawn_posix, mock_spawn_windows):
        # Define a dummy ProcessContext for testing
        process_context = ProcessContext({'PATH': 'C:\\Windows\\System32'})
        
        if is_windows:
            _spawn_windows(['cmd', '/c', 'echo', 'Hello, World!'], process_context)
            mock_spawn_posix.assert_not_called()
            mock_spawn_windows.assert_called_once_with(['cmd', '/c', 'echo', 'Hello, World!'], process_context)
        else:
            _spawn_posix(['http', 'GET', 'https://api.example.com/data'], process_context)
            mock_spawn_windows.assert_not_called()
            mock_spawn_posix.assert_called_once_with(['http', 'GET', 'https://api.example.com/data'], process_context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_internal_daemons__spawn_0_test_valid_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemons__spawn_0_test_valid_case.py:5:0: E0401: Unable to import 'httpie.contexts' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemons__spawn_0_test_valid_case.py:5:0: E0611: No name 'contexts' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemons__spawn_0_test_valid_case.py:14:11: E0602: Undefined variable 'is_windows' (undefined-variable)


"""