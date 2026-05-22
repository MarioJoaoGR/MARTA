
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin:
    def test_init(self):
        plugin = ConverterPlugin("application/test")
        assert plugin.mime == "application/test"

    @pytest.mark.parametrize("body, expected", [
        (b'\x81\xa3foo\xa3bar', ('application/json', '{"foo": "bar"}'))
    ])
    def test_convert(self, body, expected):
        plugin = ConverterPlugin("application/test")
        with pytest.raises(NotImplementedError):
            assert plugin.convert(body) == expected
