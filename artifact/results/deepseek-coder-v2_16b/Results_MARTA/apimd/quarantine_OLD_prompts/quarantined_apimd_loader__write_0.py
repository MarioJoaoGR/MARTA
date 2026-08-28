
import pytest
from unittest.mock import patch, mock_open
from apimd.loader import _write


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('builtins.open', new_callable=mock_open()) as mock_file:
            path = 'example.txt'
            doc = 'Hello, world!'
            _write(path, doc)
>           mock_file().write.assert_called_with(doc)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='open()().write' id='139985353162512'>
args = ('Hello, world!',), kwargs = {}, expected = "write('Hello, world!')"
actual = 'not called.'
error_message = "expected call not found.\nExpected: write('Hello, world!')\nActual: not called."

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\nActual: %s'
                    % (expected, actual))
>           raise AssertionError(error_message)
E           AssertionError: expected call not found.
E           Expected: write('Hello, world!')
E           Actual: not called.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:920: AssertionError
______________________________ test_invalid_path _______________________________

    def test_invalid_path():
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py::test_invalid_path
============================== 2 failed in 0.09s ===============================
"""