
import pytest
from thonny.roughparse import RoughParser


def test_edge_case():
    with pytest.raises(TypeError):
        parser = RoughParser()  # Missing arguments should raise a TypeError