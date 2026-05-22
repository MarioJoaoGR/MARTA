
import pytest
from unittest.mock import patch
from httpie.output.formatters.xml import XMLFormatter

def test_invalid_input():
    with pytest.raises(KeyError):
        formatter = XMLFormatter(format_options={'xml': {'formats': True}})
