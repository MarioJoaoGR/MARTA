
from pytutils.lazy.lazy_import import ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

def test_disallow_proxying():
    # Save the original value of _should_proxy
    original_value = ScopeReplacer._should_proxy
    
    try:
        disallow_proxying()
        assert ScopeReplacer._should_proxy == False, "Expected _should_proxy to be set to False"
        
        # Optionally, you can add more assertions or checks here if needed
    finally:
        # Restore the original value after the test
        ScopeReplacer._should_proxy = original_value
