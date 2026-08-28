
import pytest
from ansible.module_utils.common.text.converters import container_to_text

def test_container_to_text_basic():
    d = {'key1': b'value1', 'key2': 'value2'}
    result = container_to_text(d)
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {'key1': 'value1', 'key2': 'value2'}, "Conversion failed for basic case"



