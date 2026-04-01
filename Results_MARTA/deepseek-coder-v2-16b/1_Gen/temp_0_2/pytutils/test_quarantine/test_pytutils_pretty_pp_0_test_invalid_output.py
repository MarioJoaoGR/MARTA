
import pytest
from unittest.mock import patch
from pytutils.pretty import pp

@pytest.mark.parametrize("arg, lexer, formatter, outfile, expected_output", [
    ({}, 'python', 'terminal256', None, "{\n    }\n"),  # Test with empty dictionary and specific lexer/formatter
])
def test_invalid_output(arg, lexer, formatter, outfile, expected_output):
    with patch('pytutils.pretty.__PP_LEXER_PYTHON', 'python'):
        with patch('pytutils.pretty.__PP_FORMATTER', 'terminal256'):
            # Mock sys.stdout to check the output directly
            from io import StringIO
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                pp(arg, lexer=lexer, formatter=formatter, outfile=outfile)
                assert captured_output.getvalue().strip() == expected_output

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

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_invalid_output.py F [100%]

=================================== FAILURES ===================================
_________ test_invalid_output[arg0-python-terminal256-None-{\n    }\n] _________

arg = {}, lexer = 'python', formatter = 'terminal256', outfile = None
expected_output = '{\n    }\n'

    @pytest.mark.parametrize("arg, lexer, formatter, outfile, expected_output", [
        ({}, 'python', 'terminal256', None, "{\n    }\n"),  # Test with empty dictionary and specific lexer/formatter
    ])
    def test_invalid_output(arg, lexer, formatter, outfile, expected_output):
        with patch('pytutils.pretty.__PP_LEXER_PYTHON', 'python'):
            with patch('pytutils.pretty.__PP_FORMATTER', 'terminal256'):
                # Mock sys.stdout to check the output directly
                from io import StringIO
                captured_output = StringIO()
                with patch('sys.stdout', captured_output):
>                   pp(arg, lexer=lexer, formatter=formatter, outfile=outfile)

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_invalid_output.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/pretty.py:62: in pp
    pygments.highlight(arg, lexer, formatter, outfile)
/usr/local/lib/python3.11/site-packages/pygments/__init__.py:82: in highlight
    return format(lex(code, lexer), formatter, outfile)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

code = '{}', lexer = 'python'

    def lex(code, lexer):
        """
        Lex `code` with the `lexer` (must be a `Lexer` instance)
        and return an iterable of tokens. Currently, this only calls
        `lexer.get_tokens()`.
        """
        try:
>           return lexer.get_tokens(code)
E           AttributeError: 'str' object has no attribute 'get_tokens'

/usr/local/lib/python3.11/site-packages/pygments/__init__.py:42: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_invalid_output.py::test_invalid_output[arg0-python-terminal256-None-{\n    }\n]
============================== 1 failed in 0.10s ===============================
"""