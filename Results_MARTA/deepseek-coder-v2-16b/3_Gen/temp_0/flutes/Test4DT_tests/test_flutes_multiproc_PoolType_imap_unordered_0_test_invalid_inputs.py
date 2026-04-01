
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    with pytest.raises(TypeError):
        pool = PoolType()  # Create a PoolType instance without calling imap_unordered
        list(pool.imap_unordered(None, None))  # Call imap_unordered with invalid inputs
