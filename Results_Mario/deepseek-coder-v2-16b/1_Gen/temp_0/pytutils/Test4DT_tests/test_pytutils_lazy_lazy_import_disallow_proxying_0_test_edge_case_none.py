
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
    # Ensure the _should_proxy attribute is set to True initially
    assert ScopeReplacer._should_proxy == True
    
    # Call the function to disallow proxying
    disallow_proxying()
    
    # Assert that _should_proxy has been changed to False
    assert ScopeReplacer._should_proxy == False
