
import pytest
from ansible.module_utils.common.text.converters import container_to_text

def test_container_to_text_basic():
    # Basic usage scenario
    result = container_to_text({'key1': b'value1', 'key2': 'value2'})
    assert result == {'key1': 'value1', 'key2': 'value2'}
