
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    failure_try = Try(None, False)
    assert failure_try.get_or_else("default") == "default"
