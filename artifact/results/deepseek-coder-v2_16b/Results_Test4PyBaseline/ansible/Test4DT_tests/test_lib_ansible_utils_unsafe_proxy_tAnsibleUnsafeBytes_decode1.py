
# Module: ansible.utils.unsafe_proxy
import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText

# Test case 1: Basic usage of decode method
def test_basic_usage():
    byte_data = b"example_byte_string"
    unsafe_bytes_instance = AnsibleUnsafeBytes(byte_data)
    decoded_text = unsafe_bytes_instance.decode()
    assert isinstance(decoded_text, AnsibleUnsafeText), "Expected the result to be an instance of AnsibleUnsafeText"