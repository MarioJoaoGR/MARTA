
import pytest
from ansible.module_utils.common.validation import human_to_bytes

def check_type_bytes(value):
    """Convert a human-readable string value to bytes

    Raises :class:`TypeError` if unable to covert the value
    """
    try:
        return human_to_bytes(value)
    except ValueError:
        raise TypeError('%s cannot be converted to a Byte value' % type(value))


def test_invalid_input():
    value = "abc"
    with pytest.raises(TypeError):
        check_type_bytes(value)