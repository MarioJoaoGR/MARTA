# Module: sty.rendertype
# Import the function from the module
from sty.rendertype import EightbitFg

def test_EightbitFg_initialization():
    # Test initialization with a valid 8-bit number (e.g., 15, which is light gray)
    color = EightbitFg(15)
    assert isinstance(color, EightbitFg), "The object should be an instance of EightbitFg"
    assert color.args == [15], f"Expected args to be [15] but got {color.args}"

def test_EightbitFg_invalid_input():
    # Test initialization with an invalid 8-bit number (e.g., -1)
    try:
        color = EightbitFg(-1)
    except ValueError as e:
        assert str(e) == "Invalid 8-bit value, must be between 0 and 255", f"Expected a ValueError for invalid input but got {str(e)}"

def test_EightbitFg_edge_values():
    # Test initialization with the minimum valid 8-bit number (0)
    color = EightbitFg(0)
    assert isinstance(color, EightbitFg), "The object should be an instance of EightbitFg"
    assert color.args == [0], f"Expected args to be [0] but got {color.args}"
    
    # Test initialization with the maximum valid 8-bit number (255)
    color = EightbitFg(255)
    assert isinstance(color, EightbitFg), "The object should be an instance of EightbitFg"
    assert color.args == [255], f"Expected args to be [255] but got {color.args}"
