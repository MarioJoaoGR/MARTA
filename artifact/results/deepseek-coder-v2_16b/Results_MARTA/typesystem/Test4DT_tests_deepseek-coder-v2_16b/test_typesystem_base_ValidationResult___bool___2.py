
import pytest
from typesystem.base import ValidationResult, ValidationError

# Scenario 1: Test successful validation

# Scenario 2: Test failed validation due to incorrect initialization arguments
def test_failed_validation():
    with pytest.raises(TypeError):
        ValidationResult(error=ValidationError("Validation Error"))

# Scenario 3: Test the bool method of ValidationResult