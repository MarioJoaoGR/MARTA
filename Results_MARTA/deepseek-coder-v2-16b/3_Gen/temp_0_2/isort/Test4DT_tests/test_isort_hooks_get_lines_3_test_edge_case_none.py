
import pytest
from unittest.mock import patch
from isort.hooks import get_lines  # Assuming this module contains the get_lines function

@pytest.mark.parametrize("command, expected", [([], [])])
def test_edge_case_none(command, expected):
    with patch('isort.hooks.get_output', return_value='\n'.join(expected)):
        assert get_lines(command) == expected
