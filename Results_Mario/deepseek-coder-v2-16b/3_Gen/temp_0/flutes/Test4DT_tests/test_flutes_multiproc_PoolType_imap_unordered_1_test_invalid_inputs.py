
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    with pytest.raises(TypeError):
        # Assuming that imap_unordered should raise TypeError if fn is not provided
        list(pool.imap_unordered(None, range(5)))  # Providing None as the function to apply
