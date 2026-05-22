
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Conversion, ConverterPlugin

@pytest.fixture(autouse=True)
def mock_plugin_manager():
    with patch('httpie.output.processing.plugin_manager') as mock_pm:
        mock_pm.get_converters.return_value = [MagicMock()]
        yield mock_pm

@pytest.mark.parametrize("mime", ["invalid/mime", "application/json"])
def test_invalid_mime(mime):
    with patch('httpie.output.processing.is_valid_mime', return_value=True), \
         patch('httpie.output.processing.plugin_manager.get_converters') as mock_get_converters:
        mock_get_converters.return_value = []
        conversion = Conversion()
        assert conversion.get_converter(mime) is None
