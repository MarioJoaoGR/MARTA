
from pytutils.lazy.lazy_import import ImportReplacer
from unittest.mock import patch
import pytest

class TestImportProcessor:
    """Test cases for ImportProcessor class."""
    
    @patch('pytutils.lazy.lazy_import.ImportReplacer')
    def test_none_input(self, mock_import_replacer):
        """Test the behavior when no lazy_import_class is provided."""
        from pytutils.lazy.lazy_import import ImportProcessor
        
        # Create an instance without providing a lazy_import_class
        processor = ImportProcessor()
        
        # Check that the default ImportReplacer was used
        assert processor._lazy_import_class is mock_import_replacer
        
        # Ensure imports dictionary is initialized and empty
        assert processor.imports == {}

    @patch('pytutils.lazy.lazy_import.ImportReplacer')
    def test_custom_input(self, mock_import_replacer):
        """Test the behavior when a custom lazy_import_class is provided."""
        from pytutils.lazy.lazy_import import ImportProcessor
        
        # Create an instance providing a custom lazy_import_class
        class CustomImportReplacer:
            pass  # Define a minimal implementation for testing
        
        processor = ImportProcessor(lazy_import_class=CustomImportReplacer)
        
        # Check that the provided custom ImportReplacer was used
        assert processor._lazy_import_class is CustomImportReplacer
        
        # Ensure imports dictionary is initialized and empty
        assert processor.imports == {}
