
import pytest
from ansible.errors import AnsibleError
try:
    from ansible.utils.vars import _validate_mutable_mappings
except ImportError:
    # If the module is not found, skip these tests or handle appropriately
    pytest.skip("ansible.utils.vars module not available", allow_module_level=True)

def test_both_arguments_are_none():
    """Test that both arguments are None and an error is raised."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(None, None)
    assert "failed to combine variables" in str(excinfo.value)

def test_one_argument_is_none():
    """Test that one argument is None and the other is a valid mutable mapping."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(None, {'key': 'value'})
    assert "failed to combine variables" in str(excinfo.value)

def test_both_arguments_are_not_mutable_mapping():
    """Test that both arguments are not mutable mappings and an error is raised."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings([1, 2, 3], {4: 5})
    assert "failed to combine variables" in str(excinfo.value)

def test_one_argument_is_not_mutable_mapping():
    """Test that one argument is not a mutable mapping and the other is a valid mutable mapping."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings([1, 2, 3], {'key': 'value'})
    assert "failed to combine variables" in str(excinfo.value)
