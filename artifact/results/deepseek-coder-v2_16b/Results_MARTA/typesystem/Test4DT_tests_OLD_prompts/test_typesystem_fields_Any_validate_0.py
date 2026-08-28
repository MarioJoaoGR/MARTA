
import pytest
from typesystem.fields import Any

def test_valid_input():
    validator = Any()
    result = validator.validate(42)
    assert result == 42
