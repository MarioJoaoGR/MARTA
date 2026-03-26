
import pytest
from superstring.superstring import SuperString, SuperStringLower, SUPERSTRING_MINIMAL_LENGTH

class SuperStringBase:
    def __init__(self, content):
        self.content = content

    def length(self):
        return len(self.content)

    def to_printable(self):
        return self.content

    def lower(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.to_printable().lower())
        return SuperStringLower(self)

@pytest.fixture
def setup():
    s = SuperStringBase('Hello, World!')
    return s

def test_valid_input(setup):
    lower_str = setup.lower()
    assert isinstance(lower_str, SuperString)
    assert lower_str.to_printable().islower()
