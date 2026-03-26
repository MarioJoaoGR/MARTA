
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

@pytest.mark.parametrize("expected_length", [8])
def test_valid_input_default_length(expected_length):
    with patch('random.randrange') as mock_randrange:
        # Mock the return value of random.randrange to always return a fixed hex value
        mock_randrange.return_value = 0x12345678  # Example fixed hex value
        
        result = rand_hex()
        assert len(result) == expected_length
