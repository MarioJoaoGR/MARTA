
import pytest
from pymonet.semigroups import Semigroup, All



def test_invalid_inputs():
    with pytest.raises(TypeError):
        All()  # This should raise a TypeError as it's missing an argument
