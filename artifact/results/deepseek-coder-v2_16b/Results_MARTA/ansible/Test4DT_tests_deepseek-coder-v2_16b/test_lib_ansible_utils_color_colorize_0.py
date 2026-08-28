
import pytest
from ansible.utils.color import colorize, stringc


def test_edge_case():
    with pytest.raises(TypeError):
        colorize("Result", 42)
