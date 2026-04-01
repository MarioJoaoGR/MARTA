
import pytest
from flutes.iterator import MapList

def test_edge_case():
    # Create a MapList instance with a lambda function that does nothing (identity transformation)
    ml = MapList(lambda x: x, [1, 2, 3, 4, 5])
    
    # Test the length of the MapList instance
    assert len(ml) == 5
