
import pytest
from unittest.mock import patch
from httpie.utils import is_version_greater

def test_valid_case_1():
    assert is_version_greater("1.0", "0.9") == True
    assert is_version_greater("1.1", "1.2") == False
    assert is_version_greater("2.0.1", "2.0.0") == True
    assert is_version_greater("1.0.beta", "1.0.1") == False
