
import pytest
from ansible.errors import AnsibleError
try:
    from ansible.utils.vars import _validate_mutable_mappings
except ImportError:
    # If the module is not found, skip these tests or handle appropriately
    pytest.skip("ansible.utils.vars module not available", allow_module_level=True)

def test_non_dict_arguments():
    """Test that non-dictionary arguments raise an error."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings("not a dict", 123)
    assert "failed to combine variables" in str(excinfo.value)

def test_non_mutable_mapping_arguments():
    """Test that non-MutableMapping arguments raise an error."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings([1, 2, 3], {4: 5})
    assert "failed to combine variables" in str(excinfo.value)

def test_one_non_dict_argument():
    """Test that one non-dictionary argument raises an error."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings({'key': 'value'}, "not a dict")
    assert "failed to combine variables" in str(excinfo.value)

def test_none_arguments():
    """Test that None arguments raise an error."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(None, None)
    assert "failed to combine variables" in str(excinfo.value)

def test_one_none_argument():
    """Test that one None argument raises an error."""
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings({'key': 'value'}, None)
    assert "failed to combine variables" in str(excinfo.value)
