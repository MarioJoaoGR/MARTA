
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

class TestSuperStringBase:
    @pytest.fixture
    def setup(self):
        return SuperStringBase('Hello, World!')

    def test_valid_input_short_string(self, setup):
        s = setup
        lower_str = s.lower()
        assert isinstance(lower_str, SuperString)
        assert lower_str.to_printable().islower()
