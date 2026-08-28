
import pytest
from ansible.utils.version import _Alpha


def test_invalid_inputs():
    with pytest.raises(TypeError):
        _Alpha()  # No arguments provided, should raise TypeError
