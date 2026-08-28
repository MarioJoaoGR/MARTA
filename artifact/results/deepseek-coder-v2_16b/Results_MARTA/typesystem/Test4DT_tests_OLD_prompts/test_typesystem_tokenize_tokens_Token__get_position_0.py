
from typesystem.tokenize.tokens import Token
import pytest

def test_edge_case_none():
    with pytest.raises(TypeError):
        token = Token()
