
import pytest
from apimd.parser import Resolver




def test_valid_initialization():
    """Test valid initialization of the Resolver class."""
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    assert resolver.root == 'my_project'
    assert resolver.alias == {'np': 'numpy'}
    assert resolver.self_ty == 'MyClass'

def test_default_self_ty():
    """Test initialization with default self_ty value."""
    resolver = Resolver(root='my_project', alias={'np': 'numpy'})
    assert resolver.root == 'my_project'
    assert resolver.alias == {'np': 'numpy'}
    assert resolver.self_ty == ''