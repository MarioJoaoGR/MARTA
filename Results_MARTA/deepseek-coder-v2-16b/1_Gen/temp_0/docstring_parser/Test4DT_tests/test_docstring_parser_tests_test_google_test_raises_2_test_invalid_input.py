
import pytest
from docstring_parser.tests.test_google import parse  # Assuming this is the correct module path

def test_raises() -> None:
    """Test parsing raises in a Google-style docstring."""
    with pytest.raises(Exception):
        raise Exception("This will cause an exception to be raised.")
