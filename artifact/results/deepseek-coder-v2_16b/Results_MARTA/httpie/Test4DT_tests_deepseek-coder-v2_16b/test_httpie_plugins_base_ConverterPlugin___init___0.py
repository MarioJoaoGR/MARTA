
import pytest
from httpie.plugins.base import ConverterPlugin


def test_invalid_input():
    with pytest.raises(TypeError):
        ConverterPlugin()