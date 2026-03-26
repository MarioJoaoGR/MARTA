
import pytest
from unittest.mock import patch
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

class MockSuperStringBase(SuperStringBase):
    def length(self):
        return 10  # Return a value greater than SUPERSTRING_MINIMAL_LENGTH

@pytest.fixture
def valid_input():
    return MockSuperStringBase()

def test_valid_input(valid_input):
    with patch('superstring.superstring.SUPERSTRING_MINIMAL_LENGTH', 5):
        assert valid_input.upper().length() == 10
