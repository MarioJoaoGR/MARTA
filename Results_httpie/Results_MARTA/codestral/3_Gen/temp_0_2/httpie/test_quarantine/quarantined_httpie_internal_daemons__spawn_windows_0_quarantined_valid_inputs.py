
import unittest
from unittest.mock import patch, MagicMock
from httpie.internal.daemons import _spawn_windows
from httpie.contexts import ProcessContext

class TestHttpieInternalDaemonsSpawnWindows0TestValidInputs(unittest.TestCase):
    @patch('httpie.internal.daemons._start_process')
    def test_valid_inputs(self, mock_start_process):
        cmd = ['cmd', '/c', 'echo', 'Hello, World!']
        process_context = ProcessContext({'PATH': 'C:\\Windows\\System32'})
        
        _spawn_windows(cmd, process_context)
        
        # Assertions to verify the function call and its parameters
        mock_start_process.assert_called_once_with(
            cmd,
            env=process_context,
            creationflags=CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW,
            startupinfo=MagicMock()
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_internal_daemons__spawn_windows_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.contexts' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_inputs.py:5:0: E0611: No name 'contexts' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_inputs.py:19:26: E0602: Undefined variable 'CREATE_NEW_PROCESS_GROUP' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_inputs.py:19:53: E0602: Undefined variable 'CREATE_NO_WINDOW' (undefined-variable)


"""