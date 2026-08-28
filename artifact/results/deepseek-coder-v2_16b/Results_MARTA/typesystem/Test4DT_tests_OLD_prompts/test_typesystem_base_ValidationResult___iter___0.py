
import pytest
from typesystem.base import ValidationResult, ValidationError

def test_invalid_validation():
    with pytest.raises(TypeError):
        result = ValidationResult(error=ValidationError("Invalid input"))

