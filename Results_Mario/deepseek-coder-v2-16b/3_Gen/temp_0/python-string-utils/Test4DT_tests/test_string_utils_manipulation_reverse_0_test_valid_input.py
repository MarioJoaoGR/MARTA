
import pytest
from unittest.mock import patch
from string_utils.manipulation import reverse, InvalidInputError

def test_valid_input():
    with patch('string_utils.manipulation.is_string', return_value=True):
        assert reverse('hello') == 'olleh'
