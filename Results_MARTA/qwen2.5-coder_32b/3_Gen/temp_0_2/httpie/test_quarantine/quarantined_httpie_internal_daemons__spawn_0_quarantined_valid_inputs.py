
import unittest
from unittest.mock import patch, MagicMock
from httpie.internal.daemons import _spawn_windows, _spawn_posix
from httpie.contexts import ProcessContext

def test_valid_inputs():
    with patch('httpie.internal.daemons._spawn_windows', autospec=True) as mock_spawn_windows:
        with patch('httpie.internal.daemons._spawn_posix', autospec=True) as mock_spawn_posix:
            # Test when running on Windows
            process_context = ProcessContext({'PATH': 'C:\\Windows\\System32'})
            _spawn(['echo', 'Hello, World!'], process_context)
            mock_spawn_windows.assert_called_once_with(['echo', 'Hello, World!'], process_context)
            mock_spawn_posix.assert_not_called()

            # Test when running on a POSIX system (excluding MacOS)
            with patch('httpie.internal.daemons.is_windows', new=False):
                _spawn(['echo', 'Hello, World!'], process_context)
                mock_spawn_posix.assert_called_once_with(['echo', 'Hello, World!'], process_context)
                mock_spawn_windows.assert_not_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_internal_daemons__spawn_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.contexts' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_valid_inputs.py:5:0: E0611: No name 'contexts' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_valid_inputs.py:12:12: E0602: Undefined variable '_spawn' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_0_test_valid_inputs.py:18:16: E0602: Undefined variable '_spawn' (undefined-variable)


"""