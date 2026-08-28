
import pytest
from ansible.module_utils.common.network import is_masklen

def test_is_masklen_valid():
    assert is_masklen("24") == True
    assert is_masklen("0") == True
    assert is_masklen("32") == True

def test_is_masklen_invalid():
    assert is_masklen("33") == False
    assert is_masklen("-1") == False
    assert is_masklen("abc") == False
    assert is_masklen("100") == False

def test_is_masklen_non_numeric():
    assert is_masklen("twenty-four") == False
    assert is_masklen("") == False
