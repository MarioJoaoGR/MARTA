
import pytest
from flutes.multiproc import PoolState, _pool_state_init

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test invalid input by passing an integer instead of a class type
        _pool_state_init(1)
