
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    
    with pytest.raises(TypeError):
        # Calling imap_unordered without a function should raise TypeError
        list(pool.imap_unordered(None, []))  # type: ignore[arg-type]
