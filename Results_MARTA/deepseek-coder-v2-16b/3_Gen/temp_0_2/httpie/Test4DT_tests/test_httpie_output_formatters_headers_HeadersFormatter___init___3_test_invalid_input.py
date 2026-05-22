
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_invalid_input():
    with pytest.raises(Exception):
        formatter = HeadersFormatter(format_options='non-dict')
