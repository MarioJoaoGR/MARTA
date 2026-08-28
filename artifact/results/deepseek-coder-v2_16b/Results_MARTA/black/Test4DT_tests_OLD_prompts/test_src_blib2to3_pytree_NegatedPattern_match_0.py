
import pytest
from unittest.mock import MagicMock, patch
from src.blib2to3.pytree import NegatedPattern, BasePattern


def test_invalid_pattern():
    from src.blib2to3.pytree import NegatedPattern
    
    # Try to create a NegatedPattern with an invalid content type
    with pytest.raises(AssertionError):
        NegatedPattern(content="not_a_BasePattern")

def test_match_method():
    from src.blib2to3.pytree import NegatedPattern, BasePattern
    
    # Create a mock BasePattern instance
    base_pattern = MagicMock(spec=BasePattern)
    
    # Initialize NegatedPattern with the mock pattern
    np = NegatedPattern(content=base_pattern)
    
    # Test that match always returns False
    assert np.match(MagicMock()) == False