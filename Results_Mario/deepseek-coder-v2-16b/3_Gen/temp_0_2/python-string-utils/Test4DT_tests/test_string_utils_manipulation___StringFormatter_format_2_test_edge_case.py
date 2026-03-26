
from string_utils.manipulation import __StringFormatter
import pytest

@pytest.fixture
def string_formatter():
    return __StringFormatter("Initial Input String")

def test_format_string(string_formatter):
    # Test the format method of __StringFormatter class
    assert string_formatter.format() == "Initial Input String"
