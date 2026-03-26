
import pytest
from unittest.mock import MagicMock
from pymonet.semigroups import Semigroup  # Assuming this is the correct module path

# Mocking the Semigroup class
class Min(Semigroup):
    neutral_element = float('inf')
    
    def concat(self, semigroup):
        return Min(self.value if self.value <= semigroup.value else semigroup.value)

def test_error_case_1():
    # Create a mock Semigroup instance for testing
    mock_semigroup = MagicMock()
    mock_semigroup.value = 5
    
    # Create an instance of Min with a different value
    min_instance = Min(3)
    
    # Call the concat method and check the result
    combined_min = min_instance.concat(mock_semigroup)
    assert combined_min.value == 3, "Expected the smallest value to be retained"
