
import unittest
from unittest.mock import patch, MagicMock
from httpie.internal.daemons import _spawn_windows, _spawn_posix
from httpie.contexts import ProcessContext

class TestHttpieInternalDaemonsSpawn(unittest.TestCase):
    
    @patch('httpie.internal.daemons.is_windows', new=False)
    def test_edge_case(self):
        args = ['echo', 'Hello, World!']
        process_context = ProcessContext({'PATH': 'C:\\Windows\\System32'})
        
        with patch('httpie.internal.daemons._spawn_posix') as mock_spawn_posix:
            _spawn(args, process_context)
            mock_spawn_posix.assert_called_once_with(args, process_context)

    @patch('httpie.internal.daemons.is_windows', new=True)
    def test_edge_case_windows(self):
        args = ['echo', 'Hello, World!']
        process_context = ProcessContext({'PATH': 'C:\\Windows\\System32'})
        
        with patch('httpie.internal.daemons._spawn_windows') as mock_spawn_windows:
            _spawn(args, process_context)
            mock_spawn_windows.assert_called_once_with(args, process_context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_internal_daemons__spawn_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_edge_case.py:5:0: E0401: Unable to import 'httpie.contexts' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_edge_case.py:5:0: E0611: No name 'contexts' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_edge_case.py:15:12: E0602: Undefined variable '_spawn' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_edge_case.py:24:12: E0602: Undefined variable '_spawn' (undefined-variable)


"""