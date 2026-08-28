
import pytest
from apimd.parser import Parser



def test_toc_true_sets_link_to_true():
    # Setup: Real instance of Parser with toc set to True
    parser = Parser(toc=True)
    
    # Test that link is set to True when toc is True
    assert parser.link is True, "Link should be True when toc is True"


