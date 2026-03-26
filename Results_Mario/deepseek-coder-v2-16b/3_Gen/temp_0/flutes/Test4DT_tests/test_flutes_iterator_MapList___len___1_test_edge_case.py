
from flutes.iterator import MapList
import pytest

def test_edge_case():
    # Create a MapList instance with an identity function on a list of integers
    ml = MapList(lambda x: x, [1, 2, 3, 4, 5])
    
    # Check the length of the MapList instance
    assert len(ml) == 5
