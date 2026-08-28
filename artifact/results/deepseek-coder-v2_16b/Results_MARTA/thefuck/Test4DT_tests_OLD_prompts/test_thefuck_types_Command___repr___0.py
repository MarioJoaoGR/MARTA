
import pytest
from thefuck.types import Command


def test_edge_cases():
    with pytest.raises(TypeError):
        Command()