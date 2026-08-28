
import pytest
from ansible.utils.version import _Alpha

def test_valid_init():
    alpha = _Alpha("2")
    assert isinstance(alpha, _Alpha)
    assert alpha.specifier == "2"

def test_invalid_init():
    with pytest.raises(TypeError):
        _Alpha()  # This should raise a TypeError because the constructor expects one argument
