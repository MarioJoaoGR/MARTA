
import pytest
from unittest.mock import patch
from mimesis.providers.internet import Internet, Layer



def test_invalid_input():
    internet_instance = Internet(seed=42)
    with patch('mimesis.providers.internet.Internet._validate_enum', return_value=None):
        with pytest.raises(KeyError):
            protocol = internet_instance.network_protocol()