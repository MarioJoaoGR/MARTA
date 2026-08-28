
import pytest
from unittest.mock import patch
from mimesis.providers.address import Address as MimesisAddress

def test_valid_locale():
    with patch('mimesis.providers.address.Address.__init__', return_value=None):
        address = MimesisAddress(locale='en-US')
        assert isinstance(address, MimesisAddress)

def test_invalid_locale():
    with pytest.raises(ValueError):
        with patch('mimesis.providers.address.Address.__init__', side_effect=ValueError):
            address = MimesisAddress(locale='invalid-locale')

def test_missing_locale():
    with pytest.raises(TypeError):
        with patch('mimesis.providers.address.Address.__init__', side_effect=TypeError):
            address = MimesisAddress()
