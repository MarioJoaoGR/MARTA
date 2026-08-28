
import pytest
from httpie.plugins.base import TransportPlugin
from requests import adapters

# Assuming CustomAdapter is defined elsewhere in your module or library
class CustomAdapter(adapters.BaseAdapter):
    pass

class MyTransportPlugin(TransportPlugin):
    def get_adapter(self):
        return CustomAdapter()

class PrefixedTransportPlugin(TransportPlugin):
    def __init__(self, prefix):
        self.prefix = prefix
    
    def get_adapter(self):
        raise NotImplementedError()

# Test cases for TransportPlugin and its subclasses
def test_get_adapter_returns_custom_adapter():
    plugin = MyTransportPlugin()
    adapter = plugin.get_adapter()
    assert isinstance(adapter, CustomAdapter), f"Expected {CustomAdapter}, but got {type(adapter)}"

def test_get_adapter_with_prefix():
    prefix = "http://example.com"
    plugin = PrefixedTransportPlugin(prefix)
    with pytest.raises(NotImplementedError):
        adapter = plugin.get_adapter()
