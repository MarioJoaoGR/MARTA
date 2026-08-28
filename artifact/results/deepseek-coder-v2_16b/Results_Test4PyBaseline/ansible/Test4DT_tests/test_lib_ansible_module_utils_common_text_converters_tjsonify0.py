
import pytest
import json
from ansible.module_utils.common.text.converters import container_to_text, _json_encode_fallback, jsonify

# Test cases for the jsonify function
def test_jsonify_basic():
    result = jsonify({'key': b'\xe4\xf6\xfc'})
    assert isinstance(result, str), "Expected a JSON string"
    assert result == '{"key": "äöü"}', f"Unexpected result: {result}"

def test_jsonify_list():
    result = jsonify([b'\xe4\xf6\xfc', 123])
    assert isinstance(result, str), "Expected a JSON string"
    assert result == '["äöü", 123]', f"Unexpected result: {result}"

def test_jsonify_kwargs():
    result = jsonify({'key': b'\xe4\xf6\xfc'}, indent=4)
    expected_output = '{\n    "key": "äöü"\n}'
    assert isinstance(result, str), "Expected a JSON string"
    assert result == expected_output, f"Unexpected result: {result}"

def test_jsonify_invalid_encoding():
    with pytest.raises(UnicodeError):
        jsonify({'key': b'\xff\xfe'})  # Invalid encoding

def test_jsonify_fallback():
    new_data = container_to_text({b'key': b'\xe4\xf6\xfc'}, "latin-1")
    result = jsonify(new_data)
    assert isinstance(result, str), "Expected a JSON string"
    assert result == '{"key": "äöü"}', f"Unexpected result: {result}"

def test_jsonify_string():
    result = jsonify("Hello, World!")
    expected_output = '"Hello, World!"'
    assert isinstance(result, str), "Expected a JSON string"
    assert result == expected_output, f"Unexpected result: {result}"
