
import pytest
from ansible.plugins.lookup import sequence

# Fixture to create a LookupModule instance for testing
@pytest.fixture
def lookup_module():
    return sequence.LookupModule()

# Test scenario 1: Valid case with simple form
def test_valid_case_simple_form(lookup_module):
    lookup_module.args = {'start': 5, 'end': 8}
    result = list(lookup_module.generate_sequence())
    assert result == ["1", "2", "3", "4", "5"]

# Test scenario 2: Valid case with key-value form
def test_valid_case_standard_kv(lookup_module):
    lookup_module.args = {'start': 5, 'end': 11, 'stride': 2, 'format': '0x%02x'}
    result = list(lookup_module.generate_sequence())
    assert result == ["0x05", "0x07", "0x09", "0x0a"]

# Test scenario 3: Valid case with count option
def test_valid_case_count(lookup_module):
    lookup_module.args = {'count': 5}
    result = list(lookup_module.generate_sequence())
    assert result == ["1", "2", "3", "4", "5"]

# Test scenario 4: Edge case with None values
def test_edge_case_none():
    lookup_module = sequence.LookupModule()
    lookup_module.args = None
    with pytest.raises(TypeError):
        list(lookup_module.generate_sequence())

# Test scenario 5: Edge case with empty list
def test_edge_case_empty_list(lookup_module):
    lookup_module.args = {'start': 1, 'end': 0}
    result = list(lookup_module.generate_sequence())
    assert result == []

# Test scenario 6: Error case with negative stride
def test_error_case_negative_stride(lookup_module):
    lookup_module.args = {'start': 1, 'end': 10, 'stride': -2}
    with pytest.raises(ValueError):
        list(lookup_module.generate_sequence())

# Test scenario 7: Error case with invalid format string
def test_error_case_invalid_format(lookup_module):
    lookup_module.args = {'start': 1, 'format': 'invalid'}
    with pytest.raises(ValueError):
        list(lookup_module.generate_sequence())
