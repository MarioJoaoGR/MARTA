
from pytutils.lazy.lazy_import import ScopeReplacer

def test_disallow_proxying():
    """Test the disallow_proxying function."""
    from pytutils.lazy.lazy_import import disallow_proxying
    
    # Call the function to set the flag
    disallow_proxying()
    
    # Check if the flag is correctly set
    assert ScopeReplacer._should_proxy == False, "The _should_proxy flag should be set to False."
