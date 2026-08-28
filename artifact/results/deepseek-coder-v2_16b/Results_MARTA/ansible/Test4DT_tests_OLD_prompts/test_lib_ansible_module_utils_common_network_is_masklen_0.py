
import pytest
from ansible.module_utils.common.network import is_masklen

def test_is_masklen_valid():
    assert is_masklen("24") == True

def test_is_masklen_invalid_non_numeric():
    assert is_masklen("abc") == False

def test_is_masklen_invalid_out_of_range():
    assert is_masklen("33") == False
