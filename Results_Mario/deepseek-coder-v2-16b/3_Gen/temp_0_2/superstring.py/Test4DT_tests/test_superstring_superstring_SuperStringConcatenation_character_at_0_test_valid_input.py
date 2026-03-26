
import pytest
from superstring.superstring import SuperStringConcatenation, SuperString

# Fixture to create instances for testing
@pytest.fixture
def setup_concat():
    s1 = SuperString("Hello")
    s2 = SuperString(", World!")
    return SuperStringConcatenation(s1, s2)

def test_character_at(setup_concat):
    concat_str = setup_concat
    assert concat_str.character_at(0) == 'H'  # Check character at index 0
    assert concat_str.character_at(5) == ','   # Check character at index 5
    assert concat_str.character_at(12) == '!'  # Check character at index after both strings

# Run the test with pytest:
# pytest -v your_test_file.py::test_character_at
