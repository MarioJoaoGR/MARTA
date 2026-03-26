
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

def create_real_object(scope, name):
    return RealObject()  # Replace with actual object creation logic

class RealObject:
    def __init__(self, value=None):
        self.value = value

@pytest.fixture
def scope():
    return {}

@pytest.mark.parametrize("name", ["real_obj"])
def test_edge_case(scope, name):
    factory = lambda self, s, n: RealObject(n)
    replacer = ScopeReplacer(scope, factory, name)
    
    # At this point, `replacer` is a placeholder in the scope, and accessing it will trigger the creation of `RealObject`.
    assert isinstance(scope[name], RealObject)
