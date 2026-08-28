
import pytest
import json
from ansible.module_utils.common.text.converters import container_to_text

def _json_encode_fallback(obj):
    if isinstance(obj, bytes):
        return obj.decode('latin-1')
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def jsonify(data, **kwargs):
    for encoding in ("utf-8", "latin-1"):
        try:
            return json.dumps(data, encoding=encoding, default=_json_encode_fallback, **kwargs)
        except TypeError:
            try:
                new_data = container_to_text(data, encoding=encoding)
            except UnicodeDecodeError:
                continue
            return json.dumps(new_data, default=_json_encode_fallback, **kwargs)
        except UnicodeDecodeError:
            continue
    raise UnicodeError('Invalid unicode encoding encountered')

# Test function for basic functionality
def test_jsonify_basic():
    data = {'key': 'value'}
    result = jsonify(data)
    assert isinstance(result, str), "Expected a JSON string"
    assert result == '{"key": "value"}', f"Unexpected result: {result}"
