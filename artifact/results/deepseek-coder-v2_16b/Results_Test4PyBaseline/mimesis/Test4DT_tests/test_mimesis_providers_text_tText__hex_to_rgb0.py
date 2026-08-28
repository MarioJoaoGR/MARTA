
import pytest
from mimesis import Text

# Fixture to create a Text provider instance with default settings
@pytest.fixture
def text_provider():
    return Text()

# Test cases for the _hex_to_rgb method
def test_hex_to_rgb_without_hash(text_provider):
    hex_color = "1e81b0"
    rgb_color = text_provider._hex_to_rgb(hex_color)
    assert rgb_color == (30, 129, 176)

def test_hex_to_rgb_with_hash(text_provider):
    hex_color = "#1e81b0"
    rgb_color = text_provider._hex_to_rgb(hex_color)