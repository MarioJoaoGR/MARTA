
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

@pytest.mark.parametrize("input_length, expected", [
    (8, True),
    (10, True),
    (12, True),
])
def test_valid_input(input_length, expected):
    with patch('random.randrange') as mock_randrange:
        # Mock the return value of random.randrange to always return a valid hex digit sequence
        mock_randrange.return_value = 0xabcdef  # Example valid hex number
        
        result = rand_hex(input_length)
        
        assert len(result) == input_length

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""