
import unittest
from httpie.cli.nested_json.parse import tokenize, TokenKind
from unittest.mock import patch

class TestTokenize(unittest.TestCase):
    @patch('httpie.cli.nested_json.parse.OPERATORS', {'+': TokenKind.PUNCTUATION})
    def test_valid_input(self):
        source = "def my_function(): return 42"
        expected_tokens = [
            Token(kind=TokenKind.NAME, value='def', start=0, end=3),
            Token(kind=TokenKind.NAME, value='my_function', start=4, end=15),
            Token(kind=TokenKind.PUNCTUATION, value='(', start=15, end=16),
            Token(kind=TokenKind.PUNCTUATION, value=')', start=16, end=17),
            Token(kind=TokenKind.PUNCTUATION, value=':', start=17, end=18),
            Token(kind=TokenKind.NAME, value='return', start=20, end=25),
            Token(kind=TokenKind.NUMBER, value='42', start=26, end=28)
        ]
        
        tokens = list(tokenize(source))
        self.assertEqual(tokens, expected_tokens)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:7:59: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:11:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:11:23: E1101: Class 'TokenKind' has no 'NAME' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:12:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:12:23: E1101: Class 'TokenKind' has no 'NAME' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:13:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:13:23: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:14:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:14:23: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:15:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:15:23: E1101: Class 'TokenKind' has no 'PUNCTUATION' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:16:12: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:16:23: E1101: Class 'TokenKind' has no 'NAME' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_tokenize_0_test_valid_input.py:17:12: E0602: Undefined variable 'Token' (undefined-variable)


"""