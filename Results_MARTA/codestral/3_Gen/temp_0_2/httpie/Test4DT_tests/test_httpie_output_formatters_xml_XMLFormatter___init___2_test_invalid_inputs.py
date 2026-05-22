
from httpie.output.formatters.xml import XMLFormatter
import pytest

def test_invalid_inputs():
    with pytest.raises(KeyError):
        XMLFormatter()
