
import pytest
from httpie.plugins.base import FormatterPlugin

def test_invalid_input():
    with pytest.raises(KeyError):
        formatter = FormatterPlugin()
