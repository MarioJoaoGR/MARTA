
import pytest
from httpie.plugins.base import ConverterPlugin

def test_invalid_input():
    converter = ConverterPlugin("application/unknown")
    
    with pytest.raises(NotImplementedError):
        converter.convert(b"invalid input")
