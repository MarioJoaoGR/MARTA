
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    with pytest.raises(TypeError):
        # This should raise TypeError because imap_unordered expects a function and an iterable, but we are not providing any arguments
        list(pool.imap_unordered(lambda x: x**2, range(5), chunksize=1))
