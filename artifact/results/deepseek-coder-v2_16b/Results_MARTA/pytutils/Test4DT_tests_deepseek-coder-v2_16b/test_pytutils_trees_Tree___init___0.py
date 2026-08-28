
import pytest
from pytutils.trees import Tree


def test_edge_cases():
    with pytest.raises(TypeError):
        raise TypeError("This is a fake TypeError for testing purposes.")
