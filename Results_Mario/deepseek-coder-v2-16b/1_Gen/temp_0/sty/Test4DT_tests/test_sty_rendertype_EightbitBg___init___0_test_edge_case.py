
from sty.rendertype import EightbitBg

def test_edge_case():
    # Test initialization with valid edge case values (0 and 255)
    bg_color = EightbitBg(0)
    assert bg_color.args == [0]
    
    bg_color = EightbitBg(255)
    assert bg_color.args == [255]
