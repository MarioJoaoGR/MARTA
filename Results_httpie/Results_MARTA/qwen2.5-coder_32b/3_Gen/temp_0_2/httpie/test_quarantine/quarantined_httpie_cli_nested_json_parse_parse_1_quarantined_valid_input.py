
import pytest
from httpie.cli.nested_json.parse import parse, Path, Token, PathAction, TokenKind
from unittest.mock import patch

@pytest.mark.parametrize("source, expected", [
    ("root['key']path", [Path(kind=PathAction.KEY, accessor='key', tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.TEXT, value='key', start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
    ("root[123]path", [Path(kind=PathAction.INDEX, accessor=123, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.NUMBER, value=123, start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
    ("root[]path", [Path(kind=PathAction.APPEND, accessor=None, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=6, end=7)])])
])
def test_valid_input(source, expected):
    with patch('httpie.cli.nested_json.parse.tokenize', return_value=[Token(kind=TokenKind.TEXT, value='root', start=0, end=4), Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6)]):
        result = list(parse(source))
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________ test_valid_input[root['key']path-expected0] __________________

source = "root['key']path"
expected = [<httpie.cli.nested_json.tokens.Path object at 0x7f0b860c9a50>]

    @pytest.mark.parametrize("source, expected", [
        ("root['key']path", [Path(kind=PathAction.KEY, accessor='key', tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.TEXT, value='key', start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[123]path", [Path(kind=PathAction.INDEX, accessor=123, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.NUMBER, value=123, start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[]path", [Path(kind=PathAction.APPEND, accessor=None, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=6, end=7)])])
    ])
    def test_valid_input(source, expected):
        with patch('httpie.cli.nested_json.parse.tokenize', return_value=[Token(kind=TokenKind.TEXT, value='root', start=0, end=4), Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6)]):
>           result = list(parse(source))

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/nested_json/parse.py:111: in parse
    token = expect(TokenKind.TEXT, TokenKind.NUMBER, TokenKind.RIGHT_BRACKET)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

kinds = (<TokenKind.TEXT: 1>, <TokenKind.NUMBER: 2>, <TokenKind.RIGHT_BRACKET: 4>)
token = Token(kind=<TokenKind.LEFT_BRACKET: 3>, value='[', start=6, end=7)
suffix = "a text, a number or ']'"
message = "Expecting a text, a number or ']'"

    def expect(*kinds):
        nonlocal cursor
        assert kinds
        if can_advance():
            token = tokens[cursor]
            cursor += 1
            if token.kind in kinds:
                return token
        elif tokens:
            token = tokens[-1]._replace(
                start=tokens[-1].end + 0,
                end=tokens[-1].end + 1,
            )
        else:
            token = None
        if len(kinds) == 1:
            suffix = kinds[0].to_name()
        else:
            suffix = ', '.join(kind.to_name() for kind in kinds[:-1])
            suffix += ' or ' + kinds[-1].to_name()
        message = f'Expecting {suffix}'
>       raise NestedJSONSyntaxError(source, token, message)
E       httpie.cli.nested_json.errors.NestedJSONSyntaxError: HTTPie Syntax Error: Expecting a text, a number or ']'
E       root['key']path
E             ^

httpie/httpie/cli/nested_json/parse.py:67: NestedJSONSyntaxError
__________________ test_valid_input[root[123]path-expected1] ___________________

source = 'root[123]path'
expected = [<httpie.cli.nested_json.tokens.Path object at 0x7f0b855547d0>]

    @pytest.mark.parametrize("source, expected", [
        ("root['key']path", [Path(kind=PathAction.KEY, accessor='key', tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.TEXT, value='key', start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[123]path", [Path(kind=PathAction.INDEX, accessor=123, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.NUMBER, value=123, start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[]path", [Path(kind=PathAction.APPEND, accessor=None, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=6, end=7)])])
    ])
    def test_valid_input(source, expected):
        with patch('httpie.cli.nested_json.parse.tokenize', return_value=[Token(kind=TokenKind.TEXT, value='root', start=0, end=4), Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6)]):
>           result = list(parse(source))

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/nested_json/parse.py:111: in parse
    token = expect(TokenKind.TEXT, TokenKind.NUMBER, TokenKind.RIGHT_BRACKET)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

kinds = (<TokenKind.TEXT: 1>, <TokenKind.NUMBER: 2>, <TokenKind.RIGHT_BRACKET: 4>)
token = Token(kind=<TokenKind.LEFT_BRACKET: 3>, value='[', start=6, end=7)
suffix = "a text, a number or ']'"
message = "Expecting a text, a number or ']'"

    def expect(*kinds):
        nonlocal cursor
        assert kinds
        if can_advance():
            token = tokens[cursor]
            cursor += 1
            if token.kind in kinds:
                return token
        elif tokens:
            token = tokens[-1]._replace(
                start=tokens[-1].end + 0,
                end=tokens[-1].end + 1,
            )
        else:
            token = None
        if len(kinds) == 1:
            suffix = kinds[0].to_name()
        else:
            suffix = ', '.join(kind.to_name() for kind in kinds[:-1])
            suffix += ' or ' + kinds[-1].to_name()
        message = f'Expecting {suffix}'
>       raise NestedJSONSyntaxError(source, token, message)
E       httpie.cli.nested_json.errors.NestedJSONSyntaxError: HTTPie Syntax Error: Expecting a text, a number or ']'
E       root[123]path
E             ^

httpie/httpie/cli/nested_json/parse.py:67: NestedJSONSyntaxError
____________________ test_valid_input[root[]path-expected2] ____________________

source = 'root[]path'
expected = [<httpie.cli.nested_json.tokens.Path object at 0x7f0b84a04f50>]

    @pytest.mark.parametrize("source, expected", [
        ("root['key']path", [Path(kind=PathAction.KEY, accessor='key', tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.TEXT, value='key', start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[123]path", [Path(kind=PathAction.INDEX, accessor=123, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.NUMBER, value=123, start=6, end=9), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=9, end=10)])]),
        ("root[]path", [Path(kind=PathAction.APPEND, accessor=None, tokens=[Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6), Token(kind=TokenKind.RIGHT_BRACKET, value=']', start=6, end=7)])])
    ])
    def test_valid_input(source, expected):
        with patch('httpie.cli.nested_json.parse.tokenize', return_value=[Token(kind=TokenKind.TEXT, value='root', start=0, end=4), Token(kind=TokenKind.LEFT_BRACKET, value='[', start=5, end=6)]):
>           result = list(parse(source))

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/nested_json/parse.py:111: in parse
    token = expect(TokenKind.TEXT, TokenKind.NUMBER, TokenKind.RIGHT_BRACKET)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

kinds = (<TokenKind.TEXT: 1>, <TokenKind.NUMBER: 2>, <TokenKind.RIGHT_BRACKET: 4>)
token = Token(kind=<TokenKind.LEFT_BRACKET: 3>, value='[', start=6, end=7)
suffix = "a text, a number or ']'"
message = "Expecting a text, a number or ']'"

    def expect(*kinds):
        nonlocal cursor
        assert kinds
        if can_advance():
            token = tokens[cursor]
            cursor += 1
            if token.kind in kinds:
                return token
        elif tokens:
            token = tokens[-1]._replace(
                start=tokens[-1].end + 0,
                end=tokens[-1].end + 1,
            )
        else:
            token = None
        if len(kinds) == 1:
            suffix = kinds[0].to_name()
        else:
            suffix = ', '.join(kind.to_name() for kind in kinds[:-1])
            suffix += ' or ' + kinds[-1].to_name()
        message = f'Expecting {suffix}'
>       raise NestedJSONSyntaxError(source, token, message)
E       httpie.cli.nested_json.errors.NestedJSONSyntaxError: HTTPie Syntax Error: Expecting a text, a number or ']'
E       root[]path
E             ^

httpie/httpie/cli/nested_json/parse.py:67: NestedJSONSyntaxError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py::test_valid_input[root['key']path-expected0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py::test_valid_input[root[123]path-expected1]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py::test_valid_input[root[]path-expected2]
============================== 3 failed in 0.15s ===============================
"""