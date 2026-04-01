
import pytest
from string import ascii_letters, digits
import random
from unittest.mock import patch

def random_string(size: int) -> str:
    """
    Returns a string of the specified size containing random characters (uppercase/lowercase ascii letters and digits).

    *Example:*

    >>> random_string(9) # possible output: "cx3QQbzYg"

    :param size: Desired string size
    :type size: int
    :return: Random string
    """
    if not isinstance(size, int) or size < 1:
        raise ValueError('size must be >= 1')

    chars = ascii_letters + digits
    buffer = [random.choice(chars) for _ in range(size)]
    out = ''.join(buffer)

    return out

def test_invalid_input():
    with pytest.raises(ValueError):
        random_string(-1)
        random_string(0)
        random_string('a')
