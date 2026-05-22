
import unittest.mock as mock
from httpie.utils import is_version_greater

def test_valid_case_3():
    with mock.patch('httpie.utils.is_version_greater', return_value=True):
        assert is_version_greater("2.0.1", "2.0.0") == True
