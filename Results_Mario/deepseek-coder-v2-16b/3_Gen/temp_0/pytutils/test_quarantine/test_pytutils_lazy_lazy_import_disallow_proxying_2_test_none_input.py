
from pytutils.lazy.lazy_import import ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

def test_none_input():
    # Initial state check
    assert ScopeReplacer._should_proxy is True, "Precondition failed: _should_proxy should be initially True"
    
    # Call the function to disallow proxying
    disallow_proxying()
    
    # Check if the state has changed after calling the function
    assert ScopeReplacer._should_proxy is False, "Test failed: _should_proxy was not set to False by disallow_proxying"
