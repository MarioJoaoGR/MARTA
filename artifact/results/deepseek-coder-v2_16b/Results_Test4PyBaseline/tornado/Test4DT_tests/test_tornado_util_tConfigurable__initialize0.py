
import pytest
from unittest.mock import patch
from tornado.util import Configurable

# Test cases for Configurable class
def test_configurable_base():
    """Test that configurable_base returns the correct base class."""
    class MyImplementation(Configurable):
        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return MyImplementation

    # Configure the interface globally
    MyImplementation.configure(MyImplementation, key1='value1', key2='value2')
    
    my_instance = MyImplementation()
    assert isinstance(my_instance, Configurable)

def test_configurable_default():
    """Test that configurable_default returns the correct default implementation class."""
    class MyImplementation(Configurable):
        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return MyImplementation

    # Configure the interface globally
    MyImplementation.configure(MyImplementation, key1='value1', key2='value2')
    
    my_instance = MyImplementation()