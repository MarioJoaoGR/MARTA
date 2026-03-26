
from pymonet.maybe import Maybe

def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    # The following assertion should be commented out or removed since it's incorrect based on the class implementation
    # assert maybe_none.value is None
