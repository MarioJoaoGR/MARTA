
from unittest.mock import patch, MagicMock
import pytest
from apimd.parser import Parser

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_resolve_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('apimd.parser.Parser', autospec=True) as mock_parser:
            p = Parser(link=True, level=1)
            assert isinstance(p, Parser)
>           mock_parser.assert_called_with(link=True, level=1)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_resolve_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='Parser' spec='Parser' id='140006274655152'>, args = ()
kwargs = {'level': 1, 'link': True}, expected = 'Parser(link=True, level=1)'
actual = 'not called.'
error_message = 'expected call not found.\nExpected: Parser(link=True, level=1)\nActual: not called.'

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
E           Expected: Parser(link=True, level=1)
E           Actual: not called.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:920: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_resolve_0.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""