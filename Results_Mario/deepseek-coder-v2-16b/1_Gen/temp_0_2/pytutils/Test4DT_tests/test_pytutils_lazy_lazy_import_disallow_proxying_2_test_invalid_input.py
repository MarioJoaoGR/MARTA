
from unittest.mock import patch
from pytutils.lazy.lazy_import import ScopeReplacer

def test_invalid_input():
    """Test that disallow_proxying sets _should_proxy to False."""
    
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        from pytutils.lazy.lazy_import import disallow_proxying
        
        # Before calling the function, _should_proxy should be True
        assert ScopeReplacer._should_proxy is True
        
        # Call the function to set _should_proxy to False
        disallow_proxying()
        
        # After calling the function, _should_proxy should be False
        assert ScopeReplacer._should_proxy is False
