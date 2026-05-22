
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin:
    def test_init(self):
        plugin = ConverterPlugin("application/test")
        assert plugin.mime == "application/test"

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_convert_not_implemented(self):
        plugin = ConverterPlugin("application/test")
        with pytest.raises(NotImplementedError):
            plugin.convert(b"test data")
