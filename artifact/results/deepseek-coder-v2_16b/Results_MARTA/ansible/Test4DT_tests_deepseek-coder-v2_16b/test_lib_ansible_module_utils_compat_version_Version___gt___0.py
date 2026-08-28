
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion, LooseVersion, SemanticVersion

# Test for valid input in StrictVersion
def test_valid_input_strict_version():
    v = StrictVersion('1.0.4a3')
    assert str(v) == '1.0.4a3'

# Test for edge case in LooseVersion
def test_edge_case_loose_version():
    v = LooseVersion('1.5.2b2')
    assert str(v) == '1.5.2b2'

# Test for invalid input raising ValueError in SemanticVersion
def test_invalid_input_semantic_version():
    with pytest.raises(ValueError):
        v = SemanticVersion('1.0.0-alpha+build123')
