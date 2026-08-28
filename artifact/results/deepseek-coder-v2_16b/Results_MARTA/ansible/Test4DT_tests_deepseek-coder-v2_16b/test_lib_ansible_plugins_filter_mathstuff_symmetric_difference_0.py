
import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference, intersect, union
from collections.abc import Hashable


def test_edge_case():
    env = {}
    a = None
    b = []
    with pytest.raises(TypeError):
        result = symmetric_difference(env, a, b)