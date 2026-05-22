
import httpie.plugins.base as base
from unittest.mock import patch, MagicMock
import pytest

class TestConverterPlugin:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.converter = base.ConverterPlugin('application/custom-mime')

    @patch('httpie.plugins.base.ConverterPlugin.convert', return_value=('application/json', '{}'))
    def test_valid_input(self, mock_convert):
        body = b'binary data'
        new_content_type, content = self.converter.convert(body)
        assert new_content_type == 'application/json'
        assert content == '{}'
