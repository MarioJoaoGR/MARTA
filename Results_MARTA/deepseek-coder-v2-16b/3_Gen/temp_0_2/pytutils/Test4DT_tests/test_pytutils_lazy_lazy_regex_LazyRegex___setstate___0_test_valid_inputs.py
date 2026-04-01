
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    # Create an instance of LazyRegex with a valid regex pattern and flags
    lazy_regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    
    # Assert that the instance was created correctly
    assert isinstance(lazy_regex, LazyRegex)
    assert lazy_regex._regex_args == ("pattern",)
    assert lazy_regex._regex_kwargs == {"flags": 0}
