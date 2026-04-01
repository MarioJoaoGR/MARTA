
import pytest
from pymonet.box import Box

def test_edge_case():
    # Setup
    box = Box(None)
    applicativeBox = Box(lambda x: x if x is not None else 'default')
    
    # Function under test
    result = applicativeBox.ap(box)
    
    # Assertion
    assert result.value == 'default'
