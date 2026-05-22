
import pytest
from httpie.cli.nested_json.parse import tokenize, TokenKind

def test_valid_input():
    source = "def my_function():\n\treturn 42"
    tokens = list(tokenize(source))
    
    assert len(tokens) == 5
    assert tokens[0].kind == TokenKind.NAME
    assert tokens[0].value == 'def'
    assert tokens[0].start == 0
    assert tokens[0].end == 3
    
    assert tokens[1].kind == TokenKind.NAME
    assert tokens[1].value == 'my_function'
    assert tokens[1].start == 4
    assert tokens[1].end == 15
    
    assert tokens[2].kind == TokenKind.PUNCTUATION
    assert tokens[2].value == '('
    assert tokens[2].start == 15
    assert tokens[2].end == 16
    
    assert tokens[3].kind == TokenKind.PUNCTUATION
    assert tokens[3].value == ':'
    assert tokens[3].start == 17
    assert tokens[3].end == 18
    
    assert tokens[4].kind == TokenKind.NAME
    assert tokens[4].value == 'return'
    assert tokens[4].start == 20
    assert tokens[4].end == 26

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:10:29: E1101: Class 'TokenKind' has no 'NAME' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:15:29: E1101: Class 'TokenKind' has no 'NAME' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:20:29: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:25:29: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:30:29: E1101: Class 'TokenKind' has no 'NAME' member (no-member)


"""