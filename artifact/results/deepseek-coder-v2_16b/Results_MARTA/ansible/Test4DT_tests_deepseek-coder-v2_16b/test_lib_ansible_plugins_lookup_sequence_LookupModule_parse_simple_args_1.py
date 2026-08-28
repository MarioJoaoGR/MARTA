
import pytest
from ansible.plugins.lookup import sequence

@pytest.fixture(scope="module")
def lookup_module():
    return sequence.LookupModule()

# Test valid input for simple range [start-end]
def test_valid_input_simple_range(lookup_module):
    term = "5-8"
    assert lookup_module.parse_simple_args(term) is True
    assert lookup_module.start == 5
    assert lookup_module.end == 8
    assert lookup_module.stride is None
    assert lookup_module.format is None

# Test edge case where term is None
def test_edge_case_none_value(lookup_module):
    term = None
    with pytest.raises(sequence.AnsibleError, match="can't parse start=None as integer"):
        lookup_module.parse_simple_args(term)

# Test invalid input format that raises AnsibleError
def test_invalid_input_format_error(lookup_module):
    term = "5-8/invalid"
    with pytest.raises(sequence.AnsibleError, match="can't parse end=/invalid as integer"):
        lookup_module.parse_simple_args(term)
