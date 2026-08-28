
import pytest
from httpie.plugins.base import ConverterPlugin

def test_none_input():
    with pytest.raises(TypeError):
        converter = ConverterPlugin()
