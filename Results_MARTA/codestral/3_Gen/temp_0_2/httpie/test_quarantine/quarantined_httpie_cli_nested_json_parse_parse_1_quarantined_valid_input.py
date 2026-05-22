
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import parse, PathAction, TokenKind
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_valid_input():
    source = "root['key']path"
    with patch('httpie.cli.nested_json.parse.tokenize', return_value=[
        (TokenKind.TEXT, 'root'),
        (TokenKind.LEFT_BRACKET, '['),
        (TokenKind.TEXT, 'key'),
        (TokenKind.RIGHT_BRACKET, ']'),
        (TokenKind.TEXT, 'path')
    ]):
        paths = list(parse(source))
        assert len(paths) == 2
        assert paths[0].kind == PathAction.KEY
        assert paths[0].accessor == 'key'
        assert paths[1].kind == PathAction.APPEND
        assert paths[1].accessor is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        source = "root['key']path"
        with patch('httpie.cli.nested_json.parse.tokenize', return_value=[
            (TokenKind.TEXT, 'root'),
            (TokenKind.LEFT_BRACKET, '['),
            (TokenKind.TEXT, 'key'),
            (TokenKind.RIGHT_BRACKET, ']'),
            (TokenKind.TEXT, 'path')
        ]):
>           paths = list(parse(source))

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/nested_json/parse.py:106: in parse
    yield parse_root()
httpie/httpie/cli/nested_json/parse.py:79: in parse_root
    token = expect(*LITERAL_TOKENS, TokenKind.LEFT_BRACKET)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

kinds = (<TokenKind.TEXT: 1>, <TokenKind.NUMBER: 2>, <TokenKind.LEFT_BRACKET: 3>)
token = (<TokenKind.TEXT: 1>, 'root')

    def expect(*kinds):
        nonlocal cursor
        assert kinds
        if can_advance():
            token = tokens[cursor]
            cursor += 1
>           if token.kind in kinds:
E           AttributeError: 'tuple' object has no attribute 'kind'

httpie/httpie/cli/nested_json/parse.py:52: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_parse_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""