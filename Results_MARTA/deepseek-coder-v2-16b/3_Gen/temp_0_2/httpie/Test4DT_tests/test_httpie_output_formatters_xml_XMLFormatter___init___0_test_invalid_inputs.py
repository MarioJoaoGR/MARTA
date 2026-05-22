
import pytest
from httpie.output.formatters.xml import XMLFormatter

def test_invalid_inputs():
    with pytest.raises(KeyError):
        XMLFormatter()
