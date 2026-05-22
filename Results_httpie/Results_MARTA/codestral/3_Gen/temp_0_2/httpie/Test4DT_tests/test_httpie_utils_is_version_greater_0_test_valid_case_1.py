
import unittest.mock as mock
from httpie.utils import is_version_greater

def test_valid_case_1():
    with mock.patch('httpie.utils.is_version_greater', return_value=True):
        assert is_version_greater("1.0", "0.9") == True
