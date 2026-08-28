
import pytest
from requests import adapters
from httpie.plugins.base import TransportPlugin

# Scenario 1: Test that ensures get_adapter method is implemented in a subclass
def test_get_adapter_implementation():
    class MyTransportPlugin(TransportPlugin):
        pass
    
    plugin = MyTransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()

# Scenario 2: Test that verifies get_adapter returns an instance of BaseAdapter
def test_get_adapter_returns_instance():
    class MyTransportPlugin(TransportPlugin):
        def get_adapter(self):
            return adapters.HTTPAdapter()
    
    plugin = MyTransportPlugin()
    adapter = plugin.get_adapter()
    assert isinstance(adapter, adapters.BaseAdapter)

# Scenario 3: Test that ensures NotImplementedError is raised when get_adapter method is not implemented
def test_get_adapter_not_implemented():
    class MyTransportPlugin(TransportPlugin):
        pass
    
    plugin = MyTransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()
