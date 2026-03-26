# Module: pytutils.lazy.lazy_regex
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

# Test initialization with default pattern and flags
def test_init_default():
    lazy_regex = LazyRegex(args=("default_pattern", 0))
    assert lazy_regex._regex_args == ("default_pattern", 0)
    assert lazy_regex._regex_kwargs == {}

# Test initialization with custom flags using keyword arguments
def test_init_custom_flags():
    lazy_regex = LazyRegex(args=(), kwargs={"pattern": "custom_pattern", "flags": re.IGNORECASE | re.DOTALL})
    assert lazy_regex._regex_kwargs == {"pattern": "custom_pattern", "flags": re.IGNORECASE | re.DOTALL}
    assert lazy_regex._regex_args == ()

# Test changing the pattern after initialization
def test_change_pattern():
    lazy_regex = LazyRegex(args=("initial_pattern", re.IGNORECASE))
    lazy_regex._regex_args = ("new_pattern", re.IGNORECASE)
    assert lazy_regex._regex_args == ("new_pattern", re.IGNORECASE)

# Test accessing findall method which triggers regex compilation
def test_findall():
    lazy_regex = LazyRegex(args=("example pattern", 0))
    matches = lazy_regex.findall("example text with example pattern")
    assert isinstance(matches, list)  # Assuming findall returns a list of matches

# Test pickling the object
def test_pickle():
    import pickle
    lazy_regex = LazyRegex(args=("pickle_pattern", re.IGNORECASE))
    pickled_lazy_regex = pickle.dumps(lazy_regex)
    unpickled_lazy_regex = pickle.loads(pickled_lazy_regex)
    assert unpickled_lazy_regex._regex_args == ("pickle_pattern", re.IGNORECASE)
    assert unpickled_lazy_regex._regex_kwargs == {}

if __name__ == "__main__":
    pytest.main()
