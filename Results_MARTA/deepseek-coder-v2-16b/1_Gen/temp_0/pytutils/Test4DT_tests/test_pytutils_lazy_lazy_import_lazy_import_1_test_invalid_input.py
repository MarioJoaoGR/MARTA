
from unittest import mock
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
    
    with mock.patch('pytutils.lazy.lazy_import.ImportProcessor', autospec=True) as MockImportProcessor:
        # Create a mock instance of ImportProcessor
        mock_proc = MockImportProcessor.return_value
        
        # Call the function under test
        lazy_import(scope, text)
        
        # Assert that the lazy_import method was called with the correct arguments
        MockImportProcessor.assert_called_once_with(lazy_import_class=None)
        mock_proc.lazy_import.assert_called_once_with(scope, text)
