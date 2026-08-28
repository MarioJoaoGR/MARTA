
import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

def test_encode_with_valid_input():
    unsafe_text = AnsibleUnsafeText("example text")
    encoded_bytes = unsafe_text.encode()
    assert isinstance(encoded_bytes, AnsibleUnsafeBytes), "Expected encoded output to be of type AnsibleUnsafeBytes"
