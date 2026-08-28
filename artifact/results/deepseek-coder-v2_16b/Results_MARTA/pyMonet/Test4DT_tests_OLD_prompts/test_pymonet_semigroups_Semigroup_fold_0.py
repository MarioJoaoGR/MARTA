
import pytest
from unittest.mock import patch
from pymonet.semigroups import Semigroup


def test_invalid_input():
    with pytest.raises(TypeError):
        Semigroup()