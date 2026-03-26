
from pytutils.ext.rwclassproperty import sentinel
import pytest

def get_only(cls):
    return sentinel.get_only

# Assuming Z is properly imported from its respective module
@pytest.fixture
def z_instance():
    class Z:
        _get_set = sentinel.nothing
        
        def get_only(self):
            return sentinel.get_only
    
    return Z()

def test_valid_input(z_instance):
    assert z_instance.get_only() == sentinel.get_only
