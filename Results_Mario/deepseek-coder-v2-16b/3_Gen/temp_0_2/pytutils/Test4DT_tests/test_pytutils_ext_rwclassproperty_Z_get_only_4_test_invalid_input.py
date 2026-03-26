
import pytest
from pytutils.ext.rwclassproperty import sentinel

# Mocking the class Z for testing
@pytest.fixture(scope="module")
def z_instance():
    return Z()

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return sentinel.get_only

# Test case for the function
def test_get_only(z_instance):
    assert z_instance.get_only() == sentinel.get_only
