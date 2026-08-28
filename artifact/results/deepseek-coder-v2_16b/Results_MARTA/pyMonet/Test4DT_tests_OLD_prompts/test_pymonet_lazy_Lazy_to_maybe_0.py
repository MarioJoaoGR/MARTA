
import pytest
from pymonet.lazy import Lazy
from unittest.mock import patch

def test_edge_cases():
    def expensive_computation(data):
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)

    # Test with None input
    with pytest.raises(TypeError):
        maybe_result_none = lazy_object.to_maybe(None)
