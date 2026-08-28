
import pytest
from unittest.mock import patch
from mimesis.providers.internet import Internet, Layer



def test_invalid_input():
    internet = Internet()
    layer = "Invalid Layer"
    with patch('mimesis.providers.internet.Internet._validate_enum', side_effect=ValueError("Invalid Enum")):
        with pytest.raises(ValueError):
            internet.network_protocol(layer)