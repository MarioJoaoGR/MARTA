
import pytest
from unittest.mock import patch
from httpie.output.lexers.common import Lexer  # Assuming this is the correct module path

def precise(lexer, precise_token, parent_token):
    if precise_token is None or not lexer.options.get("precise"):
        return parent_token
    else:
        return precise_token

@pytest.mark.parametrize("lexer_mock, precise_token, expected", [
    (None, "CUSTOM_TOKEN", "CUSTOM_TOKEN"),  # When precise is disabled or not set
    (Lexer(), None, "DEFAULT_TOKEN"),         # When precise_token is None
    (Lexer(precise=True), "CUSTOM_TOKEN", "CUSTOM_TOKEN")  # When precise is enabled and custom token provided
])
def test_valid_inputs(lexer_mock, precise_token, expected):
    with patch('httpie.output.lexers.common.Lexer', return_value=lexer_mock):
        result = precise(lexer_mock, precise_token, "DEFAULT_TOKEN")
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_lexers_common_precise_4_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_common_precise_4_test_valid_inputs.py:4:0: E0611: No name 'Lexer' in module 'httpie.output.lexers.common' (no-name-in-module)


"""