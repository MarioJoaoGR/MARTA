
import pytest
from typesystem.tokenize.tokens import Token

def test_edge_case():
    token = Token(value="example", start_index=0, end_index=5)
    with pytest.raises(NotImplementedError):
        token._get_child_token("invalid_key")

def test_invalid_input():
    token = Token(value="example", start_index=0, end_index=5)
    with pytest.raises(NotImplementedError):
        token._get_child_token("invalid_key")
