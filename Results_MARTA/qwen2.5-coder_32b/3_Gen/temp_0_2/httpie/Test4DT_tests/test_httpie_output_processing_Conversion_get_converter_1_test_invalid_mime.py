
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.processing import Conversion, ConverterPlugin

@pytest.fixture(autouse=True)
def setup_mocks():
    with patch('httpie.output.processing.plugin_manager') as mock_plugin_manager:
        yield

def test_get_converter_invalid_mime():
    conversion = Conversion()
    result = conversion.get_converter("invalid/mime")
    assert result is None
