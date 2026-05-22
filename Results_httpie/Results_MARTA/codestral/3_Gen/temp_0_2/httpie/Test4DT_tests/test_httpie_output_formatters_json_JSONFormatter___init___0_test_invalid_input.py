
import pytest
from httpie.output.formatters.json import JSONFormatter

def test_invalid_input():
    with pytest.raises(KeyError):
        formatter = JSONFormatter()
