
import pytest
from httpie.output.formatters.xml import XMLFormatter

def test_invalid_inputs():
    with pytest.raises(KeyError):  # Expected error since format_options does not contain 'xml' key
        formatter = XMLFormatter(format_options={})
