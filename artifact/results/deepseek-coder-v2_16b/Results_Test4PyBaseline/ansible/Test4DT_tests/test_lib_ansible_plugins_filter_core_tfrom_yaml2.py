
import pytest
from ansible.plugins.filter import core
from six import string_types
import yaml

# Assuming `yaml` is a function that can load YAML data and `to_text` and `text_type` are utility functions for handling text in Python 2/3 compatibility mode

def test_from_yaml_string():
    result = core.from_yaml("key: value")
    assert result == {'key': 'value'}

def test_from_yaml_multiline_string():
    yaml_data = """
    key1: value1
    key2: value2
    """
    result = core.from_yaml(yaml_data)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_from_yaml_custom_string_wrapper():
    class MyCustomStringWrapper:
        def __init__(self, content):
            self.content = content
        
        def get_content(self):
            return self.content
    
    custom_string_wrapper = MyCustomStringWrapper("key: value")
    result = core.from_yaml(custom_string_wrapper.get_content())
    assert result == {'key': 'value'}

def test_from_yaml_non_string():
    # Assuming `yaml` can handle non-string types by returning them unchanged
    class NonString:
        pass
    
    non_string = NonString()
    result = core.from_yaml(non_string)