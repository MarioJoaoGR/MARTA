
import pytest
from typesystem.tokenize.tokens import Token

# Scenario 1: Test initialization of a token and string representation

# Scenario 2: Test raising TypeError when attempting to call a string method on an instance
def test_invalid_input():
    with pytest.raises(TypeError):
        token = Token(value="example", start_index=0, end_index=5)
        token.string()