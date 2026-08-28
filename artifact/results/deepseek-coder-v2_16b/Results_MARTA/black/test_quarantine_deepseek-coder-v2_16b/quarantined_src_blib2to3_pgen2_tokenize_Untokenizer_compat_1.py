
# content of test_src_blib2to3_pgen2_tokenize_Untokenizer_compat_1.py
from untokenizer import Untokenizer
import tokenize
import io

def test_untokenizer_initialization():
    untokenizer = Untokenizer()
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0

def test_compat_method_with_simple_code():
    code = "print('Hello, world!')"
    tokens = list(tokenize.generate_tokens(io.StringIO(code).readline))
    untokenizer = Untokenizer()
    untokenizer.compat((tokenize.NAME, 'print'), tokens)
    assert untokenizer.tokens == ['print', '(', "'Hello, world!'", ')']

def test_compat_method_with_indentation():
    code = "if True:\n    print('Inside')"
    tokens = list(tokenize.generate_tokens(io.StringIO(code).readline))
    untokenizer = Untokenizer()
    for tok in tokens:
        untokenizer.compat(tok, tokens)
    assert untokenizer.tokens == ['if True:', '    print', '(', "'Inside'", ')"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: unterminated string literal (detected at line 26) (line 26, col 77)
    assert untokenizer.tokens == ['if True:', '    print', '(', "'Inside'", ')"]
"""