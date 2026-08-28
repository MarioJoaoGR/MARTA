
import pytest
from tornado.util import Configurable

# Define a custom implementation class for demonstration purposes
class CustomImplementation:
    def __init__(self, config=None):
        self.config = config if config is not None else {}
    
    def do_something(self):
        print("Doing something with configuration:", self.config)

# Subclassing Configurable and overriding configurable_default
class CustomConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return Configurable

    @classmethod
    def configurable_default(cls):
        return CustomImplementation

def test_configurable_instantiation():
    # Configure the implementation subclass and keyword arguments
    with pytest.raises(TypeError):
        CustomConfigurable.configure(impl_class=CustomImplementation, impl_kwargs={'config': {'key': 'value'}})

def test_configurable_configure():
    # Instantiate without any configuration
    unconfigured_instance = CustomConfigurable()
    assert not hasattr(unconfigured_instance, 'config')
    
    # Configure the instance
    with pytest.raises(TypeError):
        CustomConfigurable.configure(impl_class=CustomImplementation, impl_kwargs={'config': {'key': 'value'}})

def test_configurable_inheritance():
    # Ensure that the inheritance chain is correctly followed
    class SubClass(CustomConfigurable):
        pass
    
    # Configure the subclass
    with pytest.raises(TypeError):
        SubClass.configure(impl_class=CustomImplementation, impl_kwargs={'config': {'key': 'value'}})
