
import pytest
from pymonet.immutable_list import ImmutableList

def test_error_case():
    with pytest.raises(ValueError):
        invalid_list = []
        ImmutableList().__add__(invalid_list)
