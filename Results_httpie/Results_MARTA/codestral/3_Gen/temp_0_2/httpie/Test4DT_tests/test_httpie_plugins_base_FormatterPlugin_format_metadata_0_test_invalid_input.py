
import pytest
from httpie.plugins.base import FormatterPlugin

def test_invalid_input():
    with pytest.raises(KeyError):
        # Attempt to create an instance of FormatterPlugin without providing the required 'format_options' argument
        formatter = FormatterPlugin()
