# Module: ansible.plugins.inventory.toml
import pytest
from ansible.plugins.inventory.toml import AnsibleTomlEncoder
from ansible.utils.unsafe_proxy import AnsibleSequence, AnsibleUnicode, AnsibleUnsafeBytes, AnsibleUnsafeText

# Test default initialization of the encoder
def test_default_initialization():
    encoder = AnsibleTomlEncoder()
    assert hasattr(encoder, 'dump_funcs') and isinstance(encoder.dump_funcs, dict)

# Test advanced usage with custom parameters
@pytest.mark.parametrize("preprocess_unsafe, vault_to_text", [(True, True), (False, False)])
def test_advanced_initialization(preprocess_unsafe, vault_to_text):
    encoder = AnsibleTomlEncoder(preprocess_unsafe=preprocess_unsafe, vault_to_text=vault_to_text)
    assert encoder.preprocess_unsafe == preprocess_unsafe
    assert encoder.vault_to_text == vault_to_text

# Test mapping of custom YAML object types to TOML conversion functions
def test_mapping_custom_yaml_object_types():
    encoder = AnsibleTomlEncoder()
    expected_map = {
        AnsibleSequence: encoder.dump_funcs.get(list),
        AnsibleUnicode: encoder.dump_funcs.get(str),
        AnsibleUnsafeBytes: encoder.dump_funcs.get(str),
        AnsibleUnsafeText: encoder.dump_funcs.get(str)
    }
    assert encoder.dump_funcs == expected_map
