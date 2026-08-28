
import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_basic():
    assert roman_encode(4) == 'IV'
    assert roman_encode('58') == 'LVIII'
