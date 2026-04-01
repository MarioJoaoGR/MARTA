
import pytest
from unittest.mock import patch
from pytutils.pretty import pp, __PP_LEXER_PYTHON, __PP_FORMATTER
import sys
import pygments

@pytest.mark.parametrize("arg, lexer, formatter, outfile, expected", [
    (None, None, None, None, TypeError),  # Test with None argument
    ([], None, None, None, ValueError),   # Test with empty list
    ("string", None, None, None, AttributeError),  # Test with string instead of arg
])
@patch('pytutils.pretty.__PP_LEXER_PYTHON', 'lexer')
@patch('pytutils.pretty.__PP_FORMATTER', 'formatter')
def test_edge_cases(arg, lexer, formatter, outfile, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            pp(arg, lexer=lexer, formatter=formatter, outfile=outfile)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_pretty_pp_1_test_edge_case.py FF.   [100%]

=================================== FAILURES ===================================
________________ test_edge_cases[None-None-None-None-TypeError] ________________

arg = None, lexer = None, formatter = None, outfile = None
expected = <class 'TypeError'>

    @pytest.mark.parametrize("arg, lexer, formatter, outfile, expected", [
        (None, None, None, None, TypeError),  # Test with None argument
        ([], None, None, None, ValueError),   # Test with empty list
        ("string", None, None, None, AttributeError),  # Test with string instead of arg
    ])
    @patch('pytutils.pretty.__PP_LEXER_PYTHON', 'lexer')
    @patch('pytutils.pretty.__PP_FORMATTER', 'formatter')
    def test_edge_cases(arg, lexer, formatter, outfile, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
>               pp(arg, lexer=lexer, formatter=formatter, outfile=outfile)

pytutils/Test4DT_tests/test_pytutils_pretty_pp_1_test_edge_case.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/pretty.py:62: in pp
    pygments.highlight(arg, lexer, formatter, outfile)
/usr/local/lib/python3.11/site-packages/pygments/__init__.py:82: in highlight
    return format(lex(code, lexer), formatter, outfile)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

code = 'None', lexer = None

    def lex(code, lexer):
        """
        Lex `code` with the `lexer` (must be a `Lexer` instance)
        and return an iterable of tokens. Currently, this only calls
        `lexer.get_tokens()`.
        """
        try:
>           return lexer.get_tokens(code)
E           AttributeError: 'NoneType' object has no attribute 'get_tokens'

/usr/local/lib/python3.11/site-packages/pygments/__init__.py:42: AttributeError
_______________ test_edge_cases[arg1-None-None-None-ValueError] ________________

arg = [], lexer = None, formatter = None, outfile = None
expected = <class 'ValueError'>

    @pytest.mark.parametrize("arg, lexer, formatter, outfile, expected", [
        (None, None, None, None, TypeError),  # Test with None argument
        ([], None, None, None, ValueError),   # Test with empty list
        ("string", None, None, None, AttributeError),  # Test with string instead of arg
    ])
    @patch('pytutils.pretty.__PP_LEXER_PYTHON', 'lexer')
    @patch('pytutils.pretty.__PP_FORMATTER', 'formatter')
    def test_edge_cases(arg, lexer, formatter, outfile, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
>               pp(arg, lexer=lexer, formatter=formatter, outfile=outfile)

pytutils/Test4DT_tests/test_pytutils_pretty_pp_1_test_edge_case.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/pretty.py:62: in pp
    pygments.highlight(arg, lexer, formatter, outfile)
/usr/local/lib/python3.11/site-packages/pygments/__init__.py:82: in highlight
    return format(lex(code, lexer), formatter, outfile)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

code = '[]', lexer = None

    def lex(code, lexer):
        """
        Lex `code` with the `lexer` (must be a `Lexer` instance)
        and return an iterable of tokens. Currently, this only calls
        `lexer.get_tokens()`.
        """
        try:
>           return lexer.get_tokens(code)
E           AttributeError: 'NoneType' object has no attribute 'get_tokens'

/usr/local/lib/python3.11/site-packages/pygments/__init__.py:42: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_1_test_edge_case.py::test_edge_cases[None-None-None-None-TypeError]
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_1_test_edge_case.py::test_edge_cases[arg1-None-None-None-ValueError]
========================= 2 failed, 1 passed in 0.11s ==========================
"""