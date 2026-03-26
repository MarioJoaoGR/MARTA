
# Importing necessary modules and classes
from flutes.iterator import Range  # Correctly importing the module
import pytest

def test_edge_case_none():
    """Test the edge case where no arguments are provided to the Range constructor."""
    with pytest.raises(ValueError):
        r = Range()
