
import pytest
from ansible.constants import _DeprecatedSequenceConstant


def test_invalid_input():
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant()