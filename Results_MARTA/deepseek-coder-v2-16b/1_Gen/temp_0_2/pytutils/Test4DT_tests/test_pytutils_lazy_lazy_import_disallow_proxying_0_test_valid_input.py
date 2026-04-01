
from pytutils.lazy.lazy_import import ScopeReplacer, disallow_proxying

def test_valid_input():
    # Save the original value of _should_proxy for later comparison
    original_should_proxy = ScopeReplacer._should_proxy
    
    try:
        # Call the function to set _should_proxy to False
        disallow_proxying()
        
        # Check that _should_proxy has been set to False
        assert ScopeReplacer._should_proxy == False, "Expected _should_proxy to be set to False"
    finally:
        # Restore the original value of _should_proxy (though this is usually not necessary)
        ScopeReplacer._should_proxy = original_should_proxy
