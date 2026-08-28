
import pytest
from ansible.constants import _DeprecatedSequenceConstant


def test_invalid_index():
    deprecated_constant = _DeprecatedSequenceConstant(1, "This feature will be removed in future versions.", "2.0")
    with pytest.raises(TypeError):
        deprecated_constant[0]