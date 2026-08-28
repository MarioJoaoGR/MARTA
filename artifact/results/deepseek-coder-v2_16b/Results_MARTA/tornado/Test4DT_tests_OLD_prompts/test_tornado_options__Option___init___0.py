
import pytest
from tornado.options import _Option

def test_edge_cases():
    with pytest.raises(ValueError):
        opt = _Option(name='example_option', type=None, default=[])
