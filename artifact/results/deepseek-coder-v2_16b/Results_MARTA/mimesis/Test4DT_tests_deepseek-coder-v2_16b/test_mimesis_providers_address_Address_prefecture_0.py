
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

def test_valid_prefecture_default():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='en-US')

def test_edge_prefecture_abbr():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='ja-JP')
