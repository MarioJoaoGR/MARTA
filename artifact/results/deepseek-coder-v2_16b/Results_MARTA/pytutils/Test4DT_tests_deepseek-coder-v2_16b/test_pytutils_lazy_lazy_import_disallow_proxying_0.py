
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

# Test scenarios
def test_valid_input():
    disallow_proxying()
    # No specific setup required for valid input, just calling the function
    assert True  # Assuming no errors indicate success in this context

def test_none_input():
    with pytest.raises(TypeError):
        disallow_proxying(None)  # Calling without arguments should raise TypeError

def test_invalid_input():
    with pytest.raises(TypeError):
        disallow_proxying("invalid input")  # Passing a string should raise TypeError
