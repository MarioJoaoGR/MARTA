
import pytest
from httpie.plugins.base import ConverterPlugin

@pytest.fixture
def converter_plugin():
    return ConverterPlugin('application/msgpack')

def test_convert(converter_plugin):
    with pytest.raises(NotImplementedError):
        converter_plugin.convert(b'test data')
