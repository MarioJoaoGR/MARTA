
import pytest
from httpie.output.formatters.headers import HeadersFormatter

def test_invalid_input():
    with pytest.raises(KeyError):
        HeadersFormatter()
