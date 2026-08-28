
import pytest
from httpie.plugins.base import ConverterPlugin
from unittest.mock import patch, MagicMock

def test_valid_input():
    with patch('httpie.plugins.base.ConverterPlugin.__init__', return_value=None):
        converter = ConverterPlugin('application/json')
        response_data = b'{"key": "value"}'
        with pytest.raises(NotImplementedError):
            pretty_output = converter.convert(response_data)
