
import pytest
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    with pytest.raises(TypeError):
        box = Validation()