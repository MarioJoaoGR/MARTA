
from unittest.mock import patch
from pytutils.lazy.lazy_import import lazy_import

def test_valid_input():
    scope = {}
    text = '''
    from bzrlib import (
        foo,
        bar,
        baz,
    )
    import bzrlib.branch
    import bzrlib.transport
    '''
    
    with patch('pytutils.lazy.lazy_import.ImportProcessor') as mock_proc:
        # Mock the ImportProcessor instance and its lazy_import method
        mock_instance = mock_proc.return_value
        mock_instance.lazy_import.return_value = scope
        
        result = lazy_import(scope, text)
        
        assert result == scope
