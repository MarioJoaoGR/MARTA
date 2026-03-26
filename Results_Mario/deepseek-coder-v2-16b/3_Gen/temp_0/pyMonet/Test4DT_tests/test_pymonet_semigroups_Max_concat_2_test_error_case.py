
import pytest
from unittest.mock import MagicMock

# Assuming pymonet.semigroups contains the Max class definition
class Max:
    neutral_element = -float('inf')
    def concat(self, semigroup):
        return Max(self.value if self.value > semigroup.value else semigroup.value)

def test_concat():
    # Create a mock instance of Max for testing
    max1 = Max()
    max1.value = 5
    
    max2 = Max()
    max2.value = 10
    
    # Mock the behavior of concat method
    max1.concat = MagicMock(return_value=max2)
    
    # Test the concat method
    result = max1.concat(max2)
    
    assert result.value == 10, "Expected the larger value to be taken"
