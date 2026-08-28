
import pytest
from typesystem.tokenize.tokens import Token

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Token()
