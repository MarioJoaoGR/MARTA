
from unittest.mock import patch

import pytest

from isort.hooks import get_lines  # Assuming get_lines is in isort.hooks


@pytest.mark.parametrize("command, expected", [
    (['ls', '-l'], ['total 12', '-rw-r--r--  1 user group  1024 Jan  1 12:34 file.txt', '...more lines...'])
])
def test_valid_input(command, expected):
    with patch('isort.hooks.get_output', return_value='\n'.join(expected)):
        result = get_lines(command)
        assert result == expected
