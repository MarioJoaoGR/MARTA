
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

# Fixture to provide a factory function for testing
@pytest.fixture
def my_factory():
    def factory(replacer, scope, name):
        return MyRealObject(name)  # Create the real object based on the provided name
    return factory

# Define a class that will be used as the real object
class MyRealObject:
    def __init__(self, value):
        self.value = value

    def __call__(self, arg):
        return f"Called with {arg}"

def test_scope_replacer_initialization(my_factory):
    scope = {}
    replacer = ScopeReplacer(scope, my_factory, 'my_object')
    assert 'my_object' in scope