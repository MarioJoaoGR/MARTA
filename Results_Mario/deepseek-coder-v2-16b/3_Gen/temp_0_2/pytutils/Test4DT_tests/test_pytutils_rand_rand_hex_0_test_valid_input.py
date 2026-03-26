
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

@pytest.mark.parametrize("length", [8, 10, 12])
def test_valid_input(length):
    with patch('random.randrange') as mock_randrange:
        # Mock the return value of random.randrange to always return a fixed hex string
        mock_randrange.return_value = int('a' * length, 16)
        
        result = rand_hex(length)
        assert len(result) == length
        assert all(c in '0123456789abcdef' for c in result)
