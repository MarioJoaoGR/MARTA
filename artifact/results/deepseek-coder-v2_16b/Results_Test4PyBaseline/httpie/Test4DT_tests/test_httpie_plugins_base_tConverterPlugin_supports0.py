
# Module: httpie.plugins.base
import pytest
from httpie.plugins.base import ConverterPlugin

# Test initialization with a specific MIME type
def test_converter_plugin_initialization():
    converter = ConverterPlugin(mime="application/json")
    assert converter.mime == "application/json"

# Test initialization with a custom MIME type
def test_converter_plugin_custom_mime_type():
    converter = ConverterPlugin(mime="image/png")
    assert converter.mime == "image/png"

# Test the supports method in the base class (should raise NotImplementedError)
def test_supports_method_not_implemented():
    with pytest.raises(NotImplementedError):
        converter = ConverterPlugin(mime="application/json")
        converter.supports("application/json")

# Test custom subclass implementation of supports method
class MyConverterPlugin(ConverterPlugin):
    def convert(self, content_bytes):
        # Implement your conversion logic here
        pass
    
    def supports(self, mime):  # Fixed the argument to include 'self'
        return mime == 'application/my-custom-mime-type'

def test_custom_supports_method():
    my_converter = MyConverterPlugin('application/my-custom-mime-type')
    assert my_converter.supports('application/my-custom-mime-type') is True
    assert my_converter.supports('application/another-mime-type') is False
