
import pytest
from httpie.plugins.base import ConverterPlugin
from unittest.mock import patch, MagicMock

class TestInvalidInput(ConverterPlugin):
    def convert(self, body: bytes) -> tuple[str, str]:
        raise NotImplementedError

def test_invalid_input():
    with pytest.raises(NotImplementedError):
        plugin = TestInvalidInput('application/unknown')
        plugin.convert(b'invalid input')
