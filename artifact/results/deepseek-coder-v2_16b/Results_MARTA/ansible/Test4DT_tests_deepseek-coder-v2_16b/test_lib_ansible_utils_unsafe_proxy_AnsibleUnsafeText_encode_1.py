
import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

def test_encode_invalid():
    unsafe_text = None
    with pytest.raises(AttributeError):
        encoded_bytes = unsafe_text.encode()
