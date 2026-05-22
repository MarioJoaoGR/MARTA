
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPluginSupports:
    def test_none_input(self):
        with pytest.raises(NotImplementedError):
            assert ConverterPlugin.supports(None)
