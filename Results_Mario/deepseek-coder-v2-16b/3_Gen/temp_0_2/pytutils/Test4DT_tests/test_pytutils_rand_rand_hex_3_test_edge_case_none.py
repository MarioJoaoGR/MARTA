
import pytest
import random
from unittest.mock import patch

def rand_hex(length=8):
    """
    Create a random hex string of a specific length performantly.

    :param int length: length of hex string to generate
    :return: random hex string
    """
    return '%0{}x'.format(length) % random.randrange(16**length)

@pytest.mark.parametrize("input_value", [None])
def test_edge_case_none(input_value):
    with pytest.raises(TypeError):
        rand_hex(input_value)
