
from sty import RgbFg

def test_edge_cases():
    # Define a bright green color
    green = RgbFg(0, 255, 0)
    assert green.args == [0, 255, 0]
    
    # Define a dark blue color
    blue = RgbFg(0, 0, 255)
    assert blue.args == [0, 0, 255]
