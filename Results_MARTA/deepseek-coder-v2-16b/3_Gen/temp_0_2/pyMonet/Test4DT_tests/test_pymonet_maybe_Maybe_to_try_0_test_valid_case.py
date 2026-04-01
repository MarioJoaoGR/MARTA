
import pytest
from pymonet.maybe import Maybe

def test_valid_case():
    maybe_with_value = Maybe('some_value', False)
    assert maybe_with_value.to_try().is_success is True
    assert maybe_with_value.to_try().value == 'some_value'
