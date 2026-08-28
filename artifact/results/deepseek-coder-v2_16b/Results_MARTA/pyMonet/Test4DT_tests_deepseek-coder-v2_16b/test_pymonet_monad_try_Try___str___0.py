
import pytest
from pymonet.monad_try import Try

# Test valid initialization of Try object

# Test invalid initialization that should raise TypeError
def test_invalid_initialization():
    with pytest.raises(TypeError):
        Try()  # This should raise a TypeError because the constructor expects two arguments: value and is_success