
import pytest
from pymonet.validation import Validation

# Test successful validation
def test_successful_validation():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.is_success() is True
    assert str(success_validation) == 'Validation.success[10]'

# Test failed validation with error messages

# Test invalid input where value is not None but still considered a failure due to presence of error messages