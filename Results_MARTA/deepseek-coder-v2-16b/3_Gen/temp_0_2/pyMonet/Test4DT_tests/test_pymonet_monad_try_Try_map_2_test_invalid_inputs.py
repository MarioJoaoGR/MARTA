
import pytest
from pymonet.monad_try import Try

def test_invalid_inputs():
    # Test with None as value (should raise TypeError)
    with pytest.raises(TypeError):
        Try(None, is_success=True).map(lambda x: x * 2)
