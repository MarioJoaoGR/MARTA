
import pytest
from mimesis.providers.text import Text

# Initialize the Text class with default locale and seed
@pytest.fixture
def text_generator():
    return Text()

# Test generating a random hex color without specifying safe parameter
def test_hex_color_default(text_generator):
    hex_color = text_generator.hex_color()
    assert isinstance(hex_color, str), "The output should be a string"
    assert len(hex_color) == 7, "The length of the string should be correct"
    assert hex_color[0] == '#', "The string should start with '#'"

# Test generating a random hex color specifying safe parameter as True
def test_hex_color_safe(text_generator):
    safe_hex_color = text_generator.hex_color(safe=True)
    assert isinstance(safe_hex_color, str), "The output should be a string"
    assert len(safe_hex_color) == 7, "The length of the string should be correct"
    assert safe_hex_color[0] == '#', "The string should start with '#'"
