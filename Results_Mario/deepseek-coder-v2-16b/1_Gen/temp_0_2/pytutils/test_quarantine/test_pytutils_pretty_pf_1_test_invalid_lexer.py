
import pytest
from pytutils.pretty import pf  # Import the function from your module
try:
    from pygments.lexers import PythonLexer
    from pygments.formatters import TerminalFormatter
except ImportError:
    # If Pygments is not available, we can use mock lexer and formatter or skip these tests
    class MockLexer: pass
    class MockFormatter: pass
    PythonLexer = MockLexer
    TerminalFormatter = MockFormatter

def test_invalid_lexer():
    with pytest.raises(TypeError):  # Since __PP_LEXER_PYTHON and __PP_FORMATTER are undefined, we expect a TypeError
        pf("print('Hello, World!')", lexer="invalid_lexer", formatter=TerminalFormatter())

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

pytutils/Test4DT_tests/test_pytutils_pretty_pf_1_test_invalid_lexer.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_lexer ______________________________

    def test_invalid_lexer():
        with pytest.raises(TypeError):  # Since __PP_LEXER_PYTHON and __PP_FORMATTER are undefined, we expect a TypeError
>           pf("print('Hello, World!')", lexer="invalid_lexer", formatter=TerminalFormatter())

pytutils/Test4DT_tests/test_pytutils_pretty_pf_1_test_invalid_lexer.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/pretty.py:38: in pf
    return pygments.highlight(arg, lexer, formatter)
/usr/local/lib/python3.11/site-packages/pygments/__init__.py:82: in highlight
    return format(lex(code, lexer), formatter, outfile)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

code = '"print(\'Hello, World!\')"', lexer = 'invalid_lexer'

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
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pf_1_test_invalid_lexer.py::test_invalid_lexer
============================== 1 failed in 0.10s ===============================
"""