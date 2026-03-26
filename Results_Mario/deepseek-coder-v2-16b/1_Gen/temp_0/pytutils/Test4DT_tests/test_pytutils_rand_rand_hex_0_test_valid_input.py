
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

@pytest.fixture
def valid_input():
    return rand_hex()

def test_valid_input(valid_input):
    assert len(valid_input) == 8
