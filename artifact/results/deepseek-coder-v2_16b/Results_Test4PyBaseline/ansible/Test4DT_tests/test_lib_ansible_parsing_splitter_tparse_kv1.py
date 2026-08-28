
import pytest
from ansible.parsing.splitter import parse_kv
from ansible.errors import AnsibleParserError

# Test Case 7: Handling None Input
def test_parse_kv_none_input():
    result = parse_kv(None)
    assert result == {}

# Test Case 8: Basic Usage with Spaces in Values
def test_parse_kv_spaces_in_values():
    result = parse_kv('key1=value with spaces, key2="another value", key3=\'single quoted value\'')
    expected = {'key1': 'value with spaces', 'key2': 'another value', 'key3': "single quoted value"}