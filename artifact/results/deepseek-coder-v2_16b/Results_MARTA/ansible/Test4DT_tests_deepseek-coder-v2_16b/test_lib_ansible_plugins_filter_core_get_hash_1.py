
import pytest
from ansible.plugins.filter.core import get_hash
from ansible.errors import AnsibleFilterError

# Test scenario 1: Test standard input with string and default sha1 hash type
def test_valid_case_string_sha1():
    data = 'hello world'
    expected_output = '2aae6c35c94fcfb415dbe95f408b9cef4bfc7c47'
    result = get_hash(data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Test scenario 2: Test standard input with bytes and specified sha256 hash type
def test_valid_case_bytes_sha256():
    data = b'hello world'
    hashtype = 'sha256'
    expected_output = 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    result = get_hash(data, hashtype)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Test scenario 3: Test error handling for unsupported hash type
def test_error_case_invalid_hash_type():
    data = 'hello world'
    hashtype = 'unknown_hash'
    with pytest.raises(AnsibleFilterError) as excinfo:
        get_hash(data, hashtype)
    assert str(excinfo.value) == "unsupported hash type: unknown_hash"
