
import pytest

def increase(value: int) -> int:
    """
    Return increased by 1 argument.

    :param value:
    :type value: Int
    :returns:
    :rtype: Int
    """
    return value + 1

def test_edge_case_none():
    with pytest.raises(TypeError):
        increase(None)
