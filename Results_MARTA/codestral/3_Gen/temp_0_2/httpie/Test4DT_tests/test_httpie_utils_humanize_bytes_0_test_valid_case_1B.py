
import pytest
from unittest.mock import patch
from httpie.utils import humanize_bytes

def test_valid_case_1B():
    with patch('httpie.utils.humanize_bytes', return_value='1 B'):
        assert humanize_bytes(1) == '1 B'
