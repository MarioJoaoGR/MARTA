
import pytest
from ansible.plugins.lookup.sequence import LookupModule

# Test scenarios as described

def test_valid_case_simple_form():
    seq_gen = LookupModule()
    result = seq_gen.sanity_check(start=5, end=10, stride=2, format="0x%02x")
    assert result == ["0x05", "0x07", "0x09", "0x0a"]

def test_valid_case_key_value_form():
    seq_gen = LookupModule()
    result = seq_gen.sanity_check(count=5, format="%04x")
    assert result == ["0001", "0002", "0003", "0004", "0005"]

def test_error_case_missing_parameters():
    seq_gen = LookupModule()
    with pytest.raises(Exception) as e:
        seq_gen.sanity_check(start=5, end=None, count=None)
    assert str(e.value) == "must specify count or end in with_sequence"

def test_error_case_both_parameters_specified():
    seq_gen = LookupModule()
    with pytest.raises(Exception) as e:
        seq_gen.sanity_check(start=5, end=10, count=5)
    assert str(e.value) == "can't specify both count and end in with_sequence"

def test_error_case_bad_formatting_string():
    seq_gen = LookupModule()
    with pytest.raises(Exception) as e:
        seq_gen.sanity_check(start=5, end=10, stride=2, format="bad_format")
    assert str(e.value) == "bad formatting string: bad_format"
