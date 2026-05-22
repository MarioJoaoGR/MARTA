
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin:
    def test_convert(self):
        converter = ConverterPlugin('application/msgpack')
        
        with pytest.raises(NotImplementedError):
            converter.convert(b'binary data')
