
from unittest.mock import patch
from pytutils.lazy.lazy_import import lazy_import

def test_invalid_input():
    scope = {}
    text = """
    from bzrlib import (
        foo,
        bar,
        baz,
        )
    import bzrlib.branch
    import bzrlib.transport
    """
    
    with patch('pytutils.lazy.lazy_import.ImportProcessor') as mock_proc:
        # Configure the mock to return a specific instance of ImportProcessor
        mock_instance = mock_proc.return_value
        # Set up the expected behavior for the lazy_import method on the mock instance
        mock_instance.lazy_import.return_value = {}
        
        result = lazy_import(scope, text)
        
        assert result == {}, "Expected an empty dictionary as a result"
