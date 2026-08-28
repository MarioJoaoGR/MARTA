
import pytest
from ansible.plugins.lookup import sequence as lookup_module

# Test the reset method with default values
def test_reset_default():
    lm = lookup_module.LookupModule()
    lm.reset()
    assert lm.start == 1, f"Expected start to be 1 but got {lm.start}"
    assert lm.count is None, f"Expected count to be None but got {lm.count}"
    assert lm.end is None, f"Expected end to be None but got {lm.end}"
    assert lm.stride == 1, f"Expected stride to be 1 but got {lm.stride}"
    assert lm.format == "%d", f"Expected format to be '%d' but got {lm.format}"

# Test the reset method with specific start and end values
def test_reset_with_start_and_end():
    lm = lookup_module.LookupModule()
    lm.reset()
    lm.start = 5
    lm.end = 10
    assert lm.start == 5, f"Expected start to be 5 but got {lm.start}"
    assert lm.count is None, f"Expected count to be None but got {lm.count}"
    assert lm.end == 10, f"Expected end to be 10 but got {lm.end}"
    assert lm.stride == 1, f"Expected stride to be 1 but got {lm.stride}"
    assert lm.format == "%d", f"Expected format to be '%d' but got {lm.format}"

# Test the reset method with count value
def test_reset_with_count():
    lm = lookup_module.LookupModule()
    lm.reset()
    lm.count = 5