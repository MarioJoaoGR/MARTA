
import pytest
from isort.exceptions import ISortError

def test_edge_case():
    # Test with None message
    with pytest.raises(ISortError):
        raise ISortError(None)
    
    # Test with empty string message
    with pytest.raises(ISortError):
        raise ISortError("")
