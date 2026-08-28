
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

class RealObject:
    def __init__(self, name):
        self.name = name

def create_real_object(scope, name):
    return RealObject(name)

@pytest.fixture
def setup():
    scope = {}
    replacer = ScopeReplacer(scope, create_real_object, 'real_obj')
    yield scope, replacer
    # Teardown if needed



def test_invalid_inputs():
    scope = {}
    factory = lambda scope, name: RealObject(name)
    replacer = ScopeReplacer(scope, factory, None)  # Invalid input for 'name' should raise TypeError
    with pytest.raises(TypeError):
        assert replacer()