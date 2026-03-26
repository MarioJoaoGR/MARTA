
import pytest
from unittest.mock import patch, MagicMock
from pytutils.pretty import pf, __PP_LEXER_PYTHON, __PP_FORMATTER

@pytest.mark.parametrize("input_arg", [None])
def test_none_input(input_arg):
    with patch('pytutils.pretty.pygments', MagicMock()):
        with patch('pytutils.pretty._pprint.pformat', return_value="formatted_output"):
            result = pf(input_arg)
            assert result == "formatted_output"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_pretty_pf_0_test_none_input.py F    [100%]

=================================== FAILURES ===================================
____________________________ test_none_input[None] _____________________________

input_arg = None

    @pytest.mark.parametrize("input_arg", [None])
    def test_none_input(input_arg):
        with patch('pytutils.pretty.pygments', MagicMock()):
            with patch('pytutils.pretty._pprint.pformat', return_value="formatted_output"):
                result = pf(input_arg)
>               assert result == "formatted_output"
E               AssertionError: assert <MagicMock name='mock.highlight()' id='140628709767184'> == 'formatted_output'

pytutils/Test4DT_tests/test_pytutils_pretty_pf_0_test_none_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pf_0_test_none_input.py::test_none_input[None]
============================== 1 failed in 0.09s ===============================
"""