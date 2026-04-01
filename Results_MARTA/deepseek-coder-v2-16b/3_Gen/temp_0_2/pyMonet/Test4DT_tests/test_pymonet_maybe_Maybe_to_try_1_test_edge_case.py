
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

def test_edge_case():
    maybe_none = Maybe(None, True)
    result = maybe_none.to_try()
    assert isinstance(result, Try)
    assert not result.is_success
    assert result.value is None
