
import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_valid_input():
    box = Box(42)
    try_monad = box.to_try()
    assert isinstance(try_monad, Try)
    assert try_monad.is_success is True
    assert try_monad.value == 42

def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_try()
