
# Module: sty.rendertype
# test_rendertype.py
from sty.rendertype import RgbBg

def test_rgb_bg_initialization():
    # Test initialization with valid RGB values
    rgb_bg = RgbBg(255, 0, 0)
    assert rgb_bg.args == [255, 0, 0], "Initialization with valid RGB values failed"

def test_rgb_bg_invalid_values():
    # Test initialization with invalid RGB values (out of range)
    try:
        RgbBg(-1, 0, 0)
    except ValueError as e:
        assert str(e) == "RGB components must be between 0 and 255", "Invalid RGB value not caught"
    try:
        RgbBg(256, 0, 0)
    except ValueError as e:
        assert str(e) == "RGB components must be between 0 and 255", "Invalid RGB value not caught"

def test_rgb_bg_string_representation():
    # Test string representation of the object (should return a meaningful description or code)
    rgb_bg = RgbBg(255, 0, 0)