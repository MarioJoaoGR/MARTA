
import pytest
from ansible.utils._junit_xml import _attributes

def test_none_values():
    # Test that None values are omitted from the output
    result = _attributes(x=True, y=False, z=None)
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 2, "Expected two key-value pairs excluding 'z'"
    assert list(result.keys()) == ['x', 'y'], f"Expected keys are ['x', 'y'] but got {list(result.keys())}"
