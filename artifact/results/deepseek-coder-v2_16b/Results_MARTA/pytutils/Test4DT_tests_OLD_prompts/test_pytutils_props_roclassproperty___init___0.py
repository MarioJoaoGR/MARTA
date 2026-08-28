
import pytest
from unittest.mock import patch, MagicMock
from pytutils.props import roclassproperty

# Scenario 1: Test standard input with a valid function passed to roclassproperty
def test_valid_case():
    class MyClass:
        @roclassproperty
        def my_property(cls):
            return 42
    
    assert MyClass.my_property == 42

# Scenario 2: Test with None passed as the function to roclassproperty
def test_edge_case():
    class MyClass:
        @roclassproperty
        def my_property(cls):
            return None
    
    assert MyClass.my_property is None

# Scenario 3: Test with invalid input that raises an error
def test_error_case():
    class MyClass:
        @roclassproperty
        def my_property(cls):
            raise ValueError('Invalid value')
    
    with pytest.raises(ValueError) as excinfo:
        MyClass.my_property
    assert str(excinfo.value) == 'Invalid value'
