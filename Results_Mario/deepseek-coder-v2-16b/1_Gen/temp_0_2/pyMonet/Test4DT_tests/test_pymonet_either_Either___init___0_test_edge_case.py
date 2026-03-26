
import pytest
from pymonet.either import Either, Left, Right

def test_edge_case():
    mock_either = Either(None)
    assert isinstance(mock_either, Either)
    assert mock_either.value is None
