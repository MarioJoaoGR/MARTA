
import json
from ansible.module_utils.common.jsonclass import AnsibleJSONEncoder
import pytest

# Sample data to use in tests
sample_data = {'key': 'value', 'unsafe': AnsibleUnsafe('sensitive data')}

def test_valid_input_default_settings():
    encoder = AnsibleJSONEncoder()
    json_str = json.dumps(sample_data, cls=encoder, indent=4)
    assert isinstance(json_str, str), "Expected JSON string"
    assert "'unsafe': '__ansible_unsafe__: sensitive data'" in json_str, "Expected unsafe data to be encoded as '__ansible_unsafe__: sensitive data'"

def test_valid_input_preprocess_unsafe():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    json_str = json.dumps(sample_data, cls=encoder, indent=4)
    assert isinstance(json_str, str), "Expected JSON string"
    assert "'unsafe': '__ansible_unsafe__: sensitive data'" in json_str, "Expected unsafe data to be encoded as '__ansible_unsafe__: sensitive data' with preprocessing enabled"

def test_invalid_input_error_handling():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    with pytest.raises(TypeError):
        json.dumps(None, cls=encoder, indent=4)
