
import pytest
from pymonet.utils import compose
from functools import reduce


def test_edge_cases():
    with pytest.raises(TypeError):
        compose()