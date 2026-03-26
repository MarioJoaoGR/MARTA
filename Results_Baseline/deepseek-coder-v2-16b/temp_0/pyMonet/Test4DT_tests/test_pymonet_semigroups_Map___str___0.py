
# Module: pymonet.semigroups
# test_pymonet_semigroups.py
from pymonet.semigroups import Map
import pytest

@pytest.fixture
def map_instance():
    m = Map(value=[1, 2, 3])
    return m

def test_map_str_representation(map_instance):
    assert str(map_instance) == 'Map[value=[1, 2, 3]]'
