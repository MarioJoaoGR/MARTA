
import pytest
from ansible.plugins.filter.encryption import do_unvault
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
from ansible.utils import to_native

# Test valid inputs
def test_valid_inputs():
    result = do_unvault("your_vaulted_string", "your_secret")
    assert isinstance(result, str), f"Expected a string but got {type(result)}"

# Test edge cases with None and empty values
def test_edge_cases():
    with pytest.raises(AnsibleFilterTypeError):
        do_unvault(None, "non_empty_secret")
    
    with pytest.raises(AnsibleFilterTypeError):
        do_unvault("", "")

# Test invalid inputs and error handling
def test_invalid_inputs():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        do_unvault("invalid_vault", "wrong_secret")
    assert str(excinfo.value) == "Secret passed is required to be as string, instead we got: <class 'str'>"
    
    with pytest.raises(AnsibleFilterError):
        try:
            do_unvault("invalid_vault", "wrong_secret")
        except AnsibleFilterTypeError as e:
            print(e)  # This is just to satisfy the requirement for trying and catching, not actually used in assertion
