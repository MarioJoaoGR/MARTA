
import pytest
from typesystem.tokenize.tokens import ScalarToken, Token

def test_valid_input():
    scalar_token = ScalarToken(value="example", start_index=0, end_index=5)
    assert scalar_token._get_value() == "example"

def test_edge_case_none():
    scalar_token = ScalarToken(value=None, start_index=0, end_index=5)
    assert scalar_token._get_value() is None

def test_invalid_input():
    with pytest.raises(TypeError):
        scalar_token = ScalarToken()
