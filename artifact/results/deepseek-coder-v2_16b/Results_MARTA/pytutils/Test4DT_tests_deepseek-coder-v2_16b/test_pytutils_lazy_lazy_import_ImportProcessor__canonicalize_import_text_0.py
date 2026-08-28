
import pytest
from pytutils.lazy import lazy_import
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

# Test 1: Using Default ImportReplacer

# Test 2: Using Custom Lazy Import Replacement Class
class CustomLazyImport(ImportReplacer):
    def replace_import(self, module_name):
        return f"lazy_import('{module_name}')"


# Test 3: Processing Multiple Import Statements

# Test 4: Using the _canonicalize_import_text Method
def test_canonicalize_import_text():
    processor = ImportProcessor()
    text = """
    from math import sqrt  # This is a comment and should be ignored
    import os as operating_system  # Another line with comments
    """
    canonical_imports = processor._canonicalize_import_text(text)
    assert canonical_imports == ['from math import sqrt', 'import os as operating_system']