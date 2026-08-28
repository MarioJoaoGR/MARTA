
import pytest
from ansible.module_utils.compat.version import LooseVersion

# Test valid input scenario
def test_valid_input():
    version = LooseVersion('1.5.2b2')
    assert version.version == [1, 5, '2b2']

# Test edge case scenario where None input raises TypeError
def test_edge_case():
    with pytest.raises(TypeError):
        LooseVersion(None)

# Test invalid input scenario where non-string types raise TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        LooseVersion(123)
