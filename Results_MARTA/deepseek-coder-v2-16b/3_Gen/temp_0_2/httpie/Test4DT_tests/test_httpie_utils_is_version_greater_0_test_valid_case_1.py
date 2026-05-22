
import pytest
from unittest.mock import patch
from httpie.utils import is_version_greater

def test_valid_case_1():
    with patch('httpie.utils.is_version_greater', return_value=True):
        assert is_version_greater("1.0", "0.9") == True
