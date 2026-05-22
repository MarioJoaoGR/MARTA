
import unittest
from httpie.cli.nested_json.parse import parse, Path, PathAction, TokenKind, NestedJSONSyntaxError
from unittest.mock import patch

class TestHttpieCliNestedJsonParseInvalidInput(unittest.TestCase):
    
    @patch('httpie.cli.nested_json.parse.tokenize', return_value=[
        (TokenKind.TEXT, 'root'),
        (TokenKind.LEFT_BRACKET, '['),
        (TokenKind.TEXT, 'key'),
        (TokenKind.RIGHT_BRACKET, ']'),
        (TokenKind.TEXT, 'path')
    ])
    def test_invalid_input(self, mock_tokenize):
        source = "root['key']path"
        with self.assertRaises(NestedJSONSyntaxError) as context:
            list(parse(source))
        
        error_message = str(context.exception)
        expected_error_message = "Expecting NUMBER or RIGHT_BRACKET"
        self.assertEqual(expected_error_message, error_message)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_parse_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________ TestHttpieCliNestedJsonParseInvalidInput.test_invalid_input __________

self = <test_httpie_cli_nested_json_parse_parse_0_test_invalid_input.TestHttpieCliNestedJsonParseInvalidInput testMethod=test_invalid_input>
mock_tokenize = <MagicMock name='tokenize' id='140245520654672'>

    @patch('httpie.cli.nested_json.parse.tokenize', return_value=[
        (TokenKind.TEXT, 'root'),
        (TokenKind.LEFT_BRACKET, '['),
        (TokenKind.TEXT, 'key'),
        (TokenKind.RIGHT_BRACKET, ']'),
        (TokenKind.TEXT, 'path')
    ])
    def test_invalid_input(self, mock_tokenize):
        source = "root['key']path"
        with self.assertRaises(NestedJSONSyntaxError) as context:
>           list(parse(source))

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_parse_0_test_invalid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/nested_json/parse.py:106: in parse
    yield parse_root()
httpie/httpie/cli/nested_json/parse.py:79: in parse_root
    token = expect(*LITERAL_TOKENS, TokenKind.LEFT_BRACKET)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

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
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_parse_0_test_invalid_input.py::TestHttpieCliNestedJsonParseInvalidInput::test_invalid_input
============================== 1 failed in 0.17s ===============================
"""