
import pytest
from pytutils.ext import rwclassproperty

# Assuming the sentinel object is defined in the same module or imported correctly
sentinel = rwclassproperty.sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return cls._get_set

@pytest.fixture
def z_instance():
    return Z()

def test_valid_input(z_instance):
    assert z_instance.get_only() == sentinel.nothing
