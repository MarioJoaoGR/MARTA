
import json
from ansible.module_utils.common.text.converters import to_native

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

# Test cases for jsonify function
import pytest

@pytest.mark.parametrize("data", [
    ({'key': 'value'}),
    ({'key1': b'\x80\x81'}, {'encoding': 'utf-8', 'errors': 'replace'}),
    ([{'key': 123}, b'data']),
    ({'key1': b'value1', 'key2': 'value2'})
])
def test_jsonify_basic(data):
    result = jsonify(data)
    assert isinstance(result, str), "Expected a JSON string"
    try:
        parsed = json.loads(result)
    except ValueError as e:
        pytest.fail(f"Failed to parse JSON: {e}")
