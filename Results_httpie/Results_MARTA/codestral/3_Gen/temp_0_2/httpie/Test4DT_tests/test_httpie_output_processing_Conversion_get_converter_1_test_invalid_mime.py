
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Conversion, ConverterPlugin, plugin_manager

@pytest.fixture(autouse=True)
def mock_is_valid_mime():
    with patch('httpie.output.processing.is_valid_mime', return_value=False):
        yield

def test_invalid_mime():
    conversion = Conversion()
    result = conversion.get_converter("invalid/mime")
    assert result is None
