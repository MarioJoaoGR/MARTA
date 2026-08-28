
import pytest
from typesystem.fields import DateTime

# Scenario 1: Test valid inputs

# Scenario 2: Test edge cases with year set to None

# Scenario 3: Test invalid inputs with non-numeric values
def test_invalid_inputs():
    with pytest.raises(TypeError):
        dt = DateTime(year='not_a_number', month=13, day=32, hour=25, minute=60, second=60)