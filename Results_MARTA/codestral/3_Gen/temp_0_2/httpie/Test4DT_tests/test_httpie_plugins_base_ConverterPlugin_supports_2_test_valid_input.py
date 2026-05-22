
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPluginSupports:
    def test_valid_input(self):
        with pytest.raises(NotImplementedError):
            assert ConverterPlugin.supports("application/test-mime")
