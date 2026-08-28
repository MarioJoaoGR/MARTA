
import pytest
from ansible.parsing.splitter import parse_kv
from ansible.errors import AnsibleParserError

# Test Case 1: Basic Usage
def test_parse_kv_basic():
    result = parse_kv('key1=value1, key2="value with spaces", key3=\'single quoted value\'')
    assert result == {'key1': 'value1', 'key2': 'value with spaces', 'key3': "single quoted value"}

# Test Case 2: With `check_raw` Set to True
def test_parse_kv_with_check_raw():
    result = parse_kv('key1=value1, freeform_param="free-form value", key3=\'single quoted value\'', check_raw=True)
    assert result == {'key1': 'value1', 'freeform_param': "free-form value", 'key3': "single quoted value", '_raw_params': ['freeform_param="free-form value"']}

# Test Case 3: With Escaped Characters
def test_parse_kv_escaped_chars():
    result = parse_kv('escaped=value\\=with\\,comma')
    assert result == {'escaped': 'value=with,comma'}

# Test Case 4: Empty String
def test_parse_kv_empty_string():
    result = parse_kv('')
    assert result == {}

# Test Case 5: Invalid Input (raises AnsibleParserError)
def test_parse_kv_invalid_input():
    with pytest.raises(AnsibleParserError):
        parse_kv('key1=value1, invalid input without closing quote')

# Test Case 6: Free-form parameters not added when check_raw is False
def test_parse_kv_no_freeform_without_check_raw():
    result = parse_kv('key1=value1, freeform_param="free-form value"')
    assert '_raw_params' not in result
