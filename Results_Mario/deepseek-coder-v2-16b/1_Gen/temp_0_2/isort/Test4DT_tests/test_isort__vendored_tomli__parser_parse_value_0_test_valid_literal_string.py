
import pytest
from isort._vendored.tomli._parser import parse_value
from isort._vendored.tomli._parser import Pos
from typing import Tuple, Any

@pytest.fixture
def parser():
    # You might need to mock or create a fixture that provides the necessary parser object
    pass  # Replace this with actual fixture setup if needed

def test_valid_literal_string(parser):
    src = "'this is a valid literal string'"
    pos = Pos(0)
    result = parse_value(src, pos, float)
    assert isinstance(result[1], str)
    assert result[1] == "this is a valid literal string"
